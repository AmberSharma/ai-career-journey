# AI Integration in Backend - Interview Questions

## 1. How do you integrate AI/LLM into a backend application?

You call an LLM (like GPT-4o) via its API from your backend, the same way you'd call any external service. The LLM is a third-party dependency -- your backend sends a prompt, receives a text response, and returns it to the client.

**Typical flow:**

```
Client  -->  Your Backend  -->  LLM API (OpenAI, etc.)
  POST /analyse       HTTP POST to LLM
                      with prompt + data
  <-- JSON response   <-- LLM text response
```

**What it looks like in code (Python + OpenAI SDK):**

```python
from openai import AsyncOpenAI

client = AsyncOpenAI(base_url="https://api.openai.com", api_key="sk-...")

async def analyse_logs(logs):
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a log analyst."},
            {"role": "user", "content": f"Analyse these logs:\n{logs}"},
        ],
    )
    return response.choices[0].message.content
```

**Key points to mention:**
- The LLM is just an API call -- treat it like any external service (database, payment gateway, etc.)
- Always call the LLM from the **backend**, never from the frontend (to protect API keys)
- Use **async** to avoid blocking your server while waiting for the LLM response
- Serialize your data properly before sending -- ORM objects or raw Python objects won't produce useful prompts

**One-liner:** AI integration is an API call to an LLM from your backend -- you send a prompt, get text back, and return it to the client.

---

## 2. What is a prompt? What is prompt engineering?

A **prompt** is the text input you send to an LLM to get a response. It is how you instruct the AI on what to do.

**Types of messages in a chat-based LLM:**

| Role | Purpose | Example |
|---|---|---|
| `system` | Sets the AI's behavior, role, and output format | "You are a log analyst. Return JSON with summary and recommendations." |
| `user` | The actual question or data to process | "Here are the logs: [id=1] [ERROR] Disk full..." |
| `assistant` | Previous AI responses (for multi-turn conversations) | "Based on the logs, there are 3 critical errors..." |

**Prompt engineering** is the practice of crafting prompts to get consistent, useful, and structured responses from the LLM.

**Bad prompt:**
```
Analyse these logs and give insights: [<LogDB object at 0x10f4a>, ...]
```
Problems: vague instruction, no output format specified, data not serialized.

**Good prompt:**
```
System: You are a senior DevOps log analyst. Analyse the logs and provide:
1. Summary - brief overview of the log data
2. Error Patterns - recurring errors grouped by type
3. Anomalies - anything unusual
4. Recommendations - actionable steps to fix issues

Keep your response concise and actionable.

User: Here are the application logs:
[id=1] [ERROR] Connection timeout on port 8080
[id=2] [INFO] Server started successfully
[id=3] [ERROR] Connection timeout on port 8080
```

**What makes a good prompt:**
- **Specific role** -- tell the AI who it is ("You are a log analyst")
- **Structured output** -- define exactly what sections/format you want
- **Clean data** -- serialize your data into a readable format before embedding
- **Constraints** -- "keep it concise", "return JSON", "max 5 bullet points"

**One-liner:** A prompt is the instruction you send to the LLM. Prompt engineering is about writing clear, structured prompts that produce consistent and useful output.

---

## 3. How do you handle API latency with LLM calls?

LLM API calls are slow -- typically 2-10 seconds, sometimes more. This is much slower than a database query (milliseconds). You need strategies to prevent this from degrading your application.

**Strategies:**

| Strategy | What it does | When to use |
|---|---|---|
| **Async / non-blocking** | Use `async def` + `await` so the server handles other requests while waiting for the LLM | Always -- this is the baseline |
| **Streaming** | Return the LLM response token-by-token as it generates (Server-Sent Events) | When the user is waiting and watching (chat UIs) |
| **Background jobs** | Offload the LLM call to a task queue (Celery, Redis Queue) and return a job ID immediately | When the result doesn't need to be instant |
| **Caching** | Cache LLM responses for identical/similar inputs (Redis, in-memory) | When the same data is analysed repeatedly |
| **Timeouts** | Set a max wait time; return an error if the LLM is too slow | Always -- prevents indefinite hanging |

**Async example (what we used):**

```python
# BAD -- blocks the server thread while waiting for LLM
def ai_analyse():
    response = client.chat.completions.create(...)  # blocks for 5+ seconds
    return response

# GOOD -- server handles other requests while waiting
async def ai_analyse():
    response = await client.chat.completions.create(...)  # non-blocking
    return response
```

**Streaming example:**

```python
async def stream_analysis():
    stream = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[...],
        stream=True,
    )
    async for chunk in stream:
        yield chunk.choices[0].delta.content  # send each token as it arrives
```

**Timeout example:**

```python
import httpx

client = AsyncOpenAI(
    http_client=httpx.AsyncClient(timeout=30.0),  # fail after 30 seconds
)
```

**Key line for interviews:** LLM calls are 100-1000x slower than database queries. Use async to avoid blocking, streaming for real-time UIs, caching for repeated queries, and timeouts to prevent hanging.

---

## 4. What if AI responses are unreliable or inconsistent?

LLMs are non-deterministic -- the same prompt can produce different outputs each time. You cannot treat LLM output as guaranteed structured data without safeguards.

**Common problems and solutions:**

### Problem 1: Output format varies each time

**Solution: Structured output / response format**

```python
response = await client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    response_format={"type": "json_object"},  # forces valid JSON output
)
```

Or use a JSON schema in your prompt:
```
Return your response as JSON with this exact structure:
{"summary": "...", "errors": [...], "recommendations": [...]}
```

### Problem 2: Hallucinations (AI makes things up)

**Solutions:**
- **Ground the prompt in data** -- only ask the AI to analyse data you provide, not to generate facts
- **Set temperature to 0** -- makes output more deterministic and less creative
- **Validate the output** -- parse and check the response before returning to the client

```python
response = await client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    temperature=0,  # most deterministic output
)
```

### Problem 3: LLM API is down or returns errors

**Solutions:**
- **Error handling** -- catch exceptions and return a meaningful HTTP error
- **Fallback** -- provide a basic non-AI response when the LLM is unavailable
- **Retry with backoff** -- retry failed calls with increasing delays

```python
try:
    response = await client.chat.completions.create(...)
    return response.choices[0].message.content
except Exception as e:
    raise HTTPException(status_code=502, detail=f"AI analysis failed: {str(e)}")
```

### Problem 4: Response is too long or too short

**Solutions:**
- **`max_tokens`** -- limit the response length
- **Prompt constraints** -- "respond in under 200 words", "give exactly 3 bullet points"

```python
response = await client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    max_tokens=500,  # caps the response length
)
```

**Summary of reliability techniques:**

| Technique | Purpose |
|---|---|
| `response_format={"type": "json_object"}` | Force structured JSON output |
| `temperature=0` | Reduce randomness, increase consistency |
| `max_tokens=N` | Control response length |
| Error handling (try/except) | Graceful failure instead of 500 errors |
| Output validation | Parse and verify before returning to client |
| Retry with backoff | Handle transient API failures |

**One-liner:** LLMs are non-deterministic. Use structured output formats, low temperature, validation, and error handling to make AI responses reliable enough for production use.
