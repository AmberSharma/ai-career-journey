# AI Preprocessing & Cost Optimization - Interview Questions

## 1. Why is it good to filter data before sending it to AI?

LLM APIs charge **per token** (roughly per word). Every piece of data you send costs money and adds latency. Filtering ensures the AI only receives **relevant data**, which improves accuracy, speed, and cost.

**Example from our project:**

Our `/logs/ai_analyse` endpoint analyses error logs. The database might have 10,000 logs, but only 50 are errors.

```python
# routes/logs.py
logs = get_logs("error")  # only fetch error-level logs from DB
insights = await analyse_log_with_ai(logs)
```

```python
# services/log_service.py -- filtering happens at the database level
def get_logs(type: str = None, limit: int = None):
    db = local_session()
    if type is not None:
        logs = db.query(LogDB).filter(LogDB.level == type.lower()).limit(limit).all()
    else:
        logs = db.query(LogDB).all()
    db.close()
    return logs
```

**What happens without filtering:**

| Scenario | Logs sent | Tokens (~) | Cost | Quality |
|---|---|---|---|---|
| No filter (`get_logs()`) | 10,000 logs | ~100,000 | High | AI drowns in noise, may miss patterns |
| Filtered (`get_logs("error")`) | 50 logs | ~500 | Low | AI focuses on what matters |

**Why filtering improves AI output:**
- **Less noise** -- the AI doesn't have to sift through thousands of irrelevant info/debug logs
- **Better focus** -- when every log is an error, the AI can spot patterns and group similar failures
- **Fewer hallucinations** -- with less data, the AI is less likely to invent statistics or miscount
- **Fits context window** -- LLMs have a token limit (e.g., 128K for GPT-4o). Sending an entire unfiltered database can exceed this limit and cause the request to fail

**One-liner:** Filtering before sending data to AI reduces cost, improves response quality, and prevents the model from being overwhelmed by irrelevant data.

---

## 2. How do you reduce AI cost?

LLM APIs bill based on **input tokens + output tokens**. Every optimization should aim to send fewer tokens in and get fewer tokens out.

### Strategy 1: Filter at the database level

Don't fetch everything and filter in Python. Use SQL/ORM filters so irrelevant data never leaves the database.

```python
# GOOD -- filter in the database query
logs = db.query(LogDB).filter(LogDB.level == "error").limit(100).all()

# BAD -- fetch everything, filter in Python
all_logs = db.query(LogDB).all()
error_logs = [log for log in all_logs if log.level == "error"]
```

Both give the same result for AI input, but the first approach is faster and uses less memory.

### Strategy 2: Limit the number of records

Use `.limit()` to cap how many records you send. The AI doesn't need 10,000 errors to spot a pattern -- 50-100 is usually enough.

```python
logs = get_logs("error", limit=100)  # send at most 100 logs
```

### Strategy 3: Send only relevant fields

Don't send full database records with every column. Only include what the AI needs.

```python
# BAD -- sends id, level, message, created_at, updated_at, user_id, session_id, ...
lines.append(str(log.__dict__))

# GOOD -- sends only what the AI needs to analyse
lines.append(f"[{log.level.upper()}] {log.message}")
```

Our `_serialize_logs()` function does this:
```python
def _serialize_logs(logs) -> str:
    lines = []
    for log in logs:
        lines.append(f"[id={log.id}] [{log.level.upper()}] {log.message}")
    return "\n".join(lines)
```

### Strategy 4: Use smaller, cheaper models

Not every task needs GPT-4. For log analysis, a smaller model is often sufficient.

| Model | Cost (per 1M input tokens) | When to use |
|---|---|---|
| `gpt-4o` | ~$2.50 | Complex reasoning, nuanced analysis |
| `gpt-4o-mini` | ~$0.15 | Structured tasks like log parsing, counting |
| `gpt-3.5-turbo` | ~$0.50 | Simple classification, formatting |

Our project uses `gpt-4o-mini` -- the cheapest option that still handles structured JSON output well.

### Strategy 5: Constrain the output

Use `max_tokens` to limit response length, and ask for concise output in the prompt.

```python
response = await client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    max_tokens=300,  # caps output tokens
)
```

### Strategy 6: Cache responses

If the same logs are analysed repeatedly, cache the AI response instead of calling the API again.

```python
import hashlib

cache = {}

async def analyse_with_cache(logs):
    key = hashlib.md5(str(logs).encode()).hexdigest()
    if key in cache:
        return cache[key]
    result = await analyse_log_with_ai(logs)
    cache[key] = result
    return result
```

### Cost reduction summary:

| Strategy | Token savings | Effort |
|---|---|---|
| Filter at database level | High | Low |
| Limit record count | High | Low |
| Send only relevant fields | Medium | Low |
| Use smaller models | High | None |
| Constrain output (`max_tokens`) | Medium | Low |
| Cache responses | High (on repeat calls) | Medium |

**One-liner:** Reduce AI cost by filtering data before sending, limiting record count, sending only relevant fields, using cheaper models, capping output tokens, and caching repeated queries.

---

## 3. Why not send full database records to the AI?

Sending raw, unprocessed database records to an LLM is wasteful, expensive, and produces worse results.

### Problem 1: ORM objects are not readable

```python
# What Python prints for a raw ORM object
<models.log_model.LogDB object at 0x10bd04590>
```

The LLM cannot extract any useful information from this. It's a memory address, not data.

### Problem 2: Full records contain irrelevant fields

A typical database row might have:

```json
{
    "id": 42,
    "level": "error",
    "message": "Connection timeout on port 8080",
    "created_at": "2026-04-25T10:30:00Z",
    "updated_at": "2026-04-25T10:30:00Z",
    "user_id": 17,
    "session_id": "abc123def456",
    "ip_address": "192.168.1.100",
    "request_id": "req-789",
    "stack_trace": "... 200 lines of traceback ..."
}
```

For log analysis, the AI only needs `level` and `message`. Sending everything else wastes tokens and money.

### Problem 3: Sensitive data leakage

Full records may contain:
- User IDs, email addresses, IP addresses
- Session tokens, API keys
- Personal data subject to GDPR/privacy regulations

Sending these to a third-party LLM API is a **security and compliance risk**. Filtering fields before sending ensures you don't accidentally leak sensitive data.

### Problem 4: Token limits

LLMs have context window limits. Sending 10,000 full records with 10 fields each could easily exceed the model's token limit, causing the request to fail entirely.

| Data approach | Tokens per log | 1,000 logs | 10,000 logs |
|---|---|---|---|
| Full record (10 fields) | ~80 tokens | ~80,000 | ~800,000 (exceeds most limits) |
| Serialized (level + message) | ~15 tokens | ~15,000 | ~150,000 |

### What to do instead:

```python
# BAD -- sends raw ORM objects
await analyse_log_with_ai(db.query(LogDB).all())

# GOOD -- filter, limit, and serialize
def _serialize_logs(logs) -> str:
    lines = []
    for log in logs:
        lines.append(f"[id={log.id}] [{log.level.upper()}] {log.message}")
    return "\n".join(lines)
```

**One-liner:** Don't send full DB records because they contain irrelevant fields, waste tokens, risk leaking sensitive data, and can exceed the model's context window. Always filter and serialize first.

---

## 4. What is preprocessing in the context of AI integration?

Preprocessing is **everything you do to your data between fetching it from the database and sending it to the LLM**. It transforms raw data into a clean, focused, token-efficient format that produces better AI output.

### The preprocessing pipeline:

```
Database  -->  Filter  -->  Limit  -->  Select fields  -->  Serialize  -->  LLM
```

Each step in our project:

### Step 1: Filter -- remove irrelevant records

```python
# services/log_service.py
logs = db.query(LogDB).filter(LogDB.level == "error").all()
```

Only error logs are fetched. Info, debug, and warning logs are excluded at the database level.

### Step 2: Limit -- cap the number of records

```python
logs = db.query(LogDB).filter(LogDB.level == "error").limit(100).all()
```

Even if there are 5,000 errors, the AI only gets the first 100. This keeps costs low and stays within token limits.

### Step 3: Select fields -- pick only what the AI needs

```python
# Only use id, level, and message -- ignore created_at, user_id, etc.
f"[id={log.id}] [{log.level.upper()}] {log.message}"
```

### Step 4: Serialize -- convert to a readable string format

```python
def _serialize_logs(logs) -> str:
    lines = []
    for log in logs:
        lines.append(f"[id={log.id}] [{log.level.upper()}] {log.message}")
    return "\n".join(lines)
```

This converts ORM objects into:
```
[id=1] [ERROR] Connection timeout on port 8080
[id=2] [ERROR] Disk usage at 95%
[id=3] [ERROR] Connection timeout on port 8080
```

### Step 5: Embed in a structured prompt

```python
messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": f"Here are the application logs:\n\n{formatted_logs}"},
]
```

### Without preprocessing vs with preprocessing:

**Without (raw dump):**
```
[<LogDB object at 0x10bd04590>, <LogDB object at 0x10bd04620>, ...]
```
- AI can't read it
- Contains memory addresses
- Wastes tokens
- Includes all log levels

**With preprocessing:**
```
[id=1] [ERROR] Connection timeout on port 8080
[id=2] [ERROR] Disk usage at 95%
```
- Clean, readable
- Only relevant fields
- Only error logs
- Token efficient

### Advanced preprocessing techniques:

| Technique | What it does | Example |
|---|---|---|
| **Deduplication** | Remove duplicate log messages | Group 500 identical "Connection timeout" logs into "Connection timeout (x500)" |
| **Aggregation** | Summarize before sending | "500 errors in last hour, top 3 types: timeout (300), OOM (150), auth (50)" |
| **Truncation** | Shorten long messages | Cut stack traces to first 3 lines |
| **Anonymization** | Remove PII/sensitive data | Replace IPs, emails, user IDs with placeholders |
| **Time windowing** | Only send recent logs | Filter to last 1 hour instead of all time |

### Summary:

| Preprocessing step | Purpose | Impact |
|---|---|---|
| Filter | Remove irrelevant records | Fewer tokens, better focus |
| Limit | Cap record count | Cost control, fits context window |
| Select fields | Drop unnecessary columns | Fewer tokens, no data leakage |
| Serialize | Convert to readable text | AI can actually parse the data |
| Deduplicate | Group repeated entries | Dramatically fewer tokens |
| Anonymize | Strip sensitive data | Security and compliance |

**One-liner:** Preprocessing is the pipeline of filtering, limiting, selecting fields, serializing, and cleaning your data before sending it to the LLM -- it reduces cost, improves output quality, and prevents sensitive data leakage.
