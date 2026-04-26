# AI Output, Prompts & JSON - Interview Questions

## 1. Why is AI output inconsistent?

LLMs are **non-deterministic** by design. The same prompt can produce different text, formatting, and structure each time. This is because of how the model works internally -- it picks the next word based on probabilities, not fixed rules.

**Reasons for inconsistency:**

| Reason | Explanation |
|---|---|
| **Temperature / sampling** | LLMs use a `temperature` parameter (default ~1.0) that controls randomness. Higher temperature = more creative/varied output. Even at temperature 0, minor differences can occur across API calls. |
| **No fixed output schema** | Unlike a database query that always returns rows in the same shape, an LLM returns free-form text. It might return JSON one time and markdown the next. |
| **Prompt ambiguity** | Vague prompts give the model too much freedom. "Analyse these logs" can be interpreted in many ways. |
| **Markdown wrapping** | LLMs often wrap JSON in markdown code fences (` ```json ... ``` `) even when you ask for raw JSON. This breaks `json.loads()` on the backend. |
| **Model updates** | LLM providers update models over time. The same model name (e.g., `gpt-4o-mini`) may behave slightly differently after an update. |

**Real example from our project:**

Our `/logs/ai_analyse` endpoint hit `json.JSONDecodeError: Expecting value: line 1 column 1` because the LLM sometimes returned:

```
```json
{
    "error_count": 5,
    "info_count": 12,
    "summary": "...",
    "recommendation": "..."
}
```​
```

Instead of raw JSON. The markdown fences broke `json.loads()`.

**Fix we implemented (utils/ai.py):**

```python
# Strip markdown code fences if present
cleaned = output.strip()
if cleaned.startswith("```"):
    cleaned = cleaned.split("\n", 1)[-1]   # remove ```json line
    cleaned = cleaned.rsplit("```", 1)[0]   # remove closing ```
    cleaned = cleaned.strip()

try:
    return json.loads(cleaned)
except json.JSONDecodeError:
    return {"raw_response": output}  # graceful fallback
```

**One-liner:** LLMs are probabilistic -- they pick words based on likelihood, not rules. The same prompt can produce different formats, wording, and structure each time, so your backend must validate and sanitize AI output before using it.

---

## 2. How to improve prompts for better output?

Prompt quality directly determines output quality. A vague prompt gets vague results. A structured prompt gets structured results.

### Technique 1: Give the AI a specific role

**Bad:**
```
Analyse these logs.
```

**Good:**
```
You are a backend monitoring system.
```

Why: A role narrows the AI's behavior. "Backend monitoring system" means it focuses on errors, patterns, and operational health -- not creative writing.

### Technique 2: Define the exact output format

**Bad:**
```
Give me insights about these logs.
```

**Good:**
```
Respond in JSON format:
{
    "error_count": number,
    "info_count": number,
    "summary": "short summary",
    "recommendation": "actionable suggestion"
}
```

Why: When you show the AI the exact shape of the output, it follows it consistently. Without this, it might return bullet points, paragraphs, or a table -- different every time.

### Technique 3: Serialize your data cleanly

**Bad -- passing raw ORM objects:**
```
Here are the logs: [<LogDB object at 0x10f4a>, <LogDB object at 0x10f5b>]
```

**Good -- serialized, readable format:**
```
Here are the application logs:

[id=1] [ERROR] Connection timeout on port 8080
[id=2] [INFO] Server started successfully
[id=3] [ERROR] Disk usage at 95%
```

Why: The AI can only work with what it can read. Our project does this in `_serialize_logs()`:

```python
def _serialize_logs(logs) -> str:
    lines = []
    for log in logs:
        lines.append(f"[id={log.id}] [{log.level.upper()}] {log.message}")
    return "\n".join(lines)
```

### Technique 4: Use API-level controls

```python
response = await client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    temperature=0,                              # reduce randomness
    max_tokens=500,                             # limit response length
    response_format={"type": "json_object"},    # force valid JSON
)
```

| Parameter | What it does |
|---|---|
| `temperature=0` | Makes output as deterministic as possible |
| `max_tokens` | Prevents excessively long responses |
| `response_format` | Forces the model to return valid JSON (OpenAI-specific) |

### Technique 5: Add constraints in the prompt

```
- Keep your response under 100 words
- Do not include any explanation outside the JSON
- Only analyse the logs provided, do not invent data
```

### Summary of prompt improvement techniques:

| Technique | Example |
|---|---|
| Specific role | "You are a backend monitoring system" |
| Exact output format | Show the JSON schema in the prompt |
| Clean data serialization | `[id=1] [ERROR] Connection timeout` not `<LogDB object>` |
| Low temperature | `temperature=0` for consistency |
| Response format parameter | `response_format={"type": "json_object"}` |
| Explicit constraints | "Do not include markdown fences", "respond in under 100 words" |

**One-liner:** Better prompts mean: assign a role, define the exact output structure, serialize data cleanly, use low temperature, and add explicit constraints to reduce ambiguity.

---

## 3. Why is JSON output beneficial?

When integrating AI into a backend API, the LLM's response needs to be **consumed by code**, not just read by humans. JSON makes this possible.

### Reason 1: Your API returns JSON -- the AI response must fit that contract

Your client (frontend, mobile app, another service) expects a predictable response shape:

```json
{
    "insights": {
        "error_count": 5,
        "info_count": 12,
        "summary": "High error rate on database connections",
        "recommendation": "Check database connection pool settings"
    }
}
```

If the AI returns free-form text like `"There are 5 errors and 12 info messages..."`, the frontend cannot reliably extract `error_count` or `summary` from that string. JSON gives you named fields that code can access directly.

### Reason 2: JSON is parseable and validatable

```python
# With JSON -- reliable, structured
data = json.loads(ai_output)
error_count = data["error_count"]      # always works if schema is followed
summary = data["summary"]

# Without JSON -- fragile, unpredictable
# How do you extract error_count from: "I found about 5 errors, maybe 6..."?
```

You can validate JSON against a schema, check for required fields, and reject malformed responses. You cannot do this reliably with free-form text.

### Reason 3: JSON enables downstream processing

With structured JSON, you can:

- **Store results in a database** -- each field maps to a column
- **Trigger alerts** -- `if data["error_count"] > 10: send_alert()`
- **Build dashboards** -- frontend can render charts from numeric fields
- **Compare over time** -- track how `error_count` changes across analyses

With free-form text, none of this is straightforward.

### Reason 4: JSON reduces token waste

A JSON response is compact:
```json
{"error_count": 5, "info_count": 12, "summary": "High DB errors", "recommendation": "Check pool settings"}
```

A prose response uses more tokens (and costs more):
```
After analysing the logs, I found that there are approximately 5 error-level messages
and 12 informational messages. The primary issue appears to be related to database
connection errors. I would recommend checking your connection pool settings...
```

### How to enforce JSON output:

**Option 1: In the prompt (what our project does)**
```
Respond in JSON format:
{
    "error_count": number,
    "info_count": number,
    "summary": "short summary",
    "recommendation": "actionable suggestion"
}
```

**Option 2: Using the API parameter**
```python
response = await client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    response_format={"type": "json_object"},
)
```

**Option 3: Both (most reliable)**

Use the prompt to define the schema AND the API parameter to enforce valid JSON. This gives you the best consistency.

**Always validate after parsing:**
```python
cleaned = output.strip()
if cleaned.startswith("```"):
    cleaned = cleaned.split("\n", 1)[-1]
    cleaned = cleaned.rsplit("```", 1)[0]
    cleaned = cleaned.strip()

try:
    return json.loads(cleaned)
except json.JSONDecodeError:
    return {"raw_response": output}
```

### Summary:

| Benefit | Why it matters |
|---|---|
| **API contract compliance** | Your REST API returns JSON -- AI output must match |
| **Parseable by code** | `data["error_count"]` vs regex on free text |
| **Validatable** | Check required fields, types, and values |
| **Enables automation** | Alerts, dashboards, storage, comparisons |
| **Token efficient** | Structured data is more compact than prose |

**One-liner:** JSON output lets your backend code reliably parse, validate, store, and act on AI responses -- free-form text cannot be consumed programmatically without fragile parsing.
