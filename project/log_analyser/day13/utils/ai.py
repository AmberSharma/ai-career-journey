import httpx
from openai import AsyncOpenAI
from fastapi import HTTPException
from config import LITELLM_BASE_URL, LITELLM_API_KEY, AI_CONFIGURED
import json

client = None
if AI_CONFIGURED:
    client = AsyncOpenAI(
        base_url=LITELLM_BASE_URL,
        api_key=LITELLM_API_KEY,
        http_client=httpx.AsyncClient(verify=False),
    )

SYSTEM_PROMPT = """You are a backend monitoring system.

Analyse the following logs and respond in JSON format:

{{
    "error_count": number,
    "info_count": number,
    "summary": "short summary",
    "recommendation": "actionable suggestion"
}}
"""


def _serialize_logs(logs) -> str:
    """Convert LogDB ORM objects to a readable string for the LLM prompt."""
    lines = []
    for log in logs:
        lines.append(f"[id={log.id}] [{log.level.upper()}] {log.message}")
    return "\n".join(lines)


async def analyse_log_with_ai(logs):
    if not client:
        raise HTTPException(
            status_code=503,
            detail="AI analysis is unavailable. LITELLM_BASE_URL and LITELLM_API_KEY environment variables are not set.",
        )

    if not logs:
        return "No logs found in the database. Nothing to analyse."

    formatted_logs = _serialize_logs(logs)

    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Here are the application logs:\n\n{formatted_logs}"},
            ],
        )
        output = response.choices[0].message.content
        print(output)
        if not output:
            raise HTTPException(status_code=502, detail="AI returned an empty response.")

        # Strip mark down code fences if present (e.g. ```json ... ```)
        cleaned = output.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[-1]   # remove first line (```json)
            cleaned = cleaned.rsplit("```", 1)[0]   # remove closing ```
            cleaned = cleaned.strip()

        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return {"raw_response": output}

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"AI analysis failed: {str(e)}",
        )
