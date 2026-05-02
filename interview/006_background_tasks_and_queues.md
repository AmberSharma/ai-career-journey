# Background Tasks, Async & Queues - Interview Questions

## 1. Why use background tasks?

Background tasks let you **return a response to the client immediately** while doing work in the background. Without them, the client waits until all processing is finished, which leads to slow response times and poor user experience.

**Common use cases:**
- Sending emails or notifications after a user action
- Running AI analysis that takes several seconds
- Writing audit logs or analytics
- Processing file uploads (thumbnails, parsing)

**Example from our project:**

Our `/logs/ai-background` endpoint triggers AI analysis of error logs. The AI call can take 5-10 seconds. Instead of making the user wait, we return immediately and process in the background:

```python
# routes/logs.py
@router.post("/logs/ai-background")
def ai_background(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_ai_analysis)
    return {"message": "AI task started in background"}
```

Without background tasks, the client would hang for the entire duration of the AI call. With them, the client gets a response in milliseconds.

**Key point:** Background tasks are for work that the client doesn't need to wait for. If the client needs the result in the response, use a normal (or async) endpoint instead.

---

## 2. Are background tasks scalable?

**Short answer:** FastAPI's `BackgroundTasks` are **not scalable** for production workloads. They work fine for lightweight, low-volume tasks but have real limitations.

**Why they don't scale:**

| Limitation | Explanation |
|---|---|
| **Tied to the process** | Tasks run inside the same FastAPI server process. If the server crashes or restarts, in-flight tasks are lost silently. |
| **No retries** | If a task fails (network error, API timeout), it's gone. There is no built-in retry mechanism. |
| **No visibility** | You can't check the status of a background task. There's no task ID, no progress tracking, no way to know if it succeeded or failed (unless you build that yourself). |
| **Resource contention** | Background tasks share CPU and memory with your request-handling code. Heavy background work can slow down your API responses. |
| **Single server only** | Tasks can't be distributed across multiple worker machines. You're limited to the capacity of one server. |

**When `BackgroundTasks` are fine:**
- Development and prototyping
- Low-traffic internal tools
- Lightweight tasks (logging, sending a single email)

**When you need something more robust:**
- High traffic or mission-critical tasks -> use a task queue (Celery, Bull, etc.)
- Tasks that must not be lost -> use a message broker with persistence (Redis, RabbitMQ)

---

## 3. Difference between async and background tasks?

These are **two separate concepts** that are often confused. They solve different problems.

### Async (`async`/`await`)

Async is about **non-blocking I/O within a request**. When you `await` an async call, the event loop is free to handle other incoming requests while waiting for I/O (database query, API call, file read). The **client still waits** for the response.

```python
# The client waits for the full AI response before getting a result
@router.post("/logs/ai_analyse")
async def ai_analyse():
    logs = get_logs("error")
    insights = await analyse_log_with_ai(logs)  # non-blocking wait
    return {"insights": insights}
```

- The server can handle other requests while waiting for the AI API.
- But the client that made this request is still waiting for the response.

### Background Tasks

Background tasks **detach work from the request-response cycle entirely**. The client gets a response immediately, and the work happens afterward.

```python
# The client gets an instant response; AI runs later
@router.post("/logs/ai-background")
def ai_background(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_ai_analysis)
    return {"message": "AI task started in background"}
```

### Side-by-side comparison

| | `async`/`await` | Background Tasks |
|---|---|---|
| **Purpose** | Non-blocking I/O within a request | Detach work from the response |
| **Client waits?** | Yes, client waits for the response | No, client gets an immediate response |
| **Result returned?** | Yes, directly in the response | No, result is not sent to the client |
| **Server efficiency** | Event loop handles other requests during I/O waits | Task runs after the response is sent |
| **Use when** | Client needs the result | Client doesn't need the result right away |

**They can work together.** A background task function can be `async` and use `await` internally:

```python
async def run_ai_analysis():
    error_logs = get_logs("error")
    if error_logs:
        insights = await analyse_log_with_ai(error_logs)  # async inside background task
        print("insights", insights)
```

This gives you both: the client doesn't wait (background task), and the server stays efficient during I/O (async).

---

## 4. When would we use queues?

Use a task queue when `BackgroundTasks` isn't enough — specifically when you need **reliability, scalability, or visibility**.

### Situations that demand a queue

**1. Tasks that must not be lost**
If the server crashes, `BackgroundTasks` lose all in-flight work. A queue (backed by Redis/RabbitMQ) persists tasks. Workers pick them up even after restarts.

**2. Tasks that need retries**
API calls fail. Networks time out. Queues like Celery have built-in retry policies with exponential backoff:

```python
@celery_app.task(bind=True, max_retries=3, default_retry_delay=60)
def analyse_logs_task(self, log_ids):
    try:
        results = call_ai_api(log_ids)
        save_results(results)
    except APIError as e:
        self.retry(exc=e)
```

**3. High volume or heavy processing**
When tasks are CPU-intensive or numerous, running them in the API server degrades response times. Queues offload work to **dedicated worker processes** (potentially on separate machines).

**4. Task status tracking**
Users want to know if their export is "processing", "complete", or "failed". Queues provide task IDs and status tracking out of the box.

**5. Rate limiting and prioritization**
Queues let you control concurrency (e.g., only 5 AI calls at a time) and prioritize certain tasks over others.

### Common queue technologies

| Technology | Language | Broker | Best for |
|---|---|---|---|
| **Celery** | Python | Redis / RabbitMQ | General-purpose Python task queues |
| **Bull / BullMQ** | Node.js | Redis | Node.js applications |
| **RQ (Redis Queue)** | Python | Redis | Simple Python queues |
| **AWS SQS + Lambda** | Any | AWS managed | Serverless architectures |

### Decision guide

```
Do you need the result in the HTTP response?
  -> Yes: Use async/await (no background task needed)
  -> No: Is the task lightweight and loss-acceptable?
      -> Yes: Use BackgroundTasks
      -> No: Use a task queue (Celery, Bull, etc.)
```

**Example:** In our project, `BackgroundTasks` works for now because we're just printing AI insights to the console. But if we needed to store results, notify users, and guarantee delivery, we'd move to Celery + Redis.
