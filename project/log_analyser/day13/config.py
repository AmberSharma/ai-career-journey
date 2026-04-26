import os
from dotenv import load_dotenv

load_dotenv()

LITELLM_BASE_URL = os.environ.get("LITELLM_BASE_URL")
LITELLM_API_KEY = os.environ.get("LITELLM_API_KEY")

AI_CONFIGURED = bool(LITELLM_BASE_URL and LITELLM_API_KEY)

if not AI_CONFIGURED:
    print(
        "WARNING: LITELLM_BASE_URL and/or LITELLM_API_KEY not set. "
        "The /logs/ai_analyse endpoint will not work until they are exported."
    )