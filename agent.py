import os
import json
import anthropic
import re
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def clean_json(text):
    text = text.strip()

    # remove markdown ```json ```
    text = text.replace("```json", "").replace("```", "")

    # extract only JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)

    return None


def parse_command(command):
    prompt = f"""
You are a strict JSON generator.

Convert the user command into JSON.

Command: {command}

If user wants to send ETH:
{{
  "action": "send_eth",
  "amount": number,
  "address": "string"
}}

If user asks for balance:
{{
  "action": "get_balance"
}}

{{
  "action": "send_eth",
  "amount": number,
  "address": "string"
}}
"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response.content[0].text

    print("RAW CLAUDE OUTPUT:\n", content)  # debug

    # 👇 CLEAN JSON
    json_text = clean_json(content)

    if not json_text:
        raise Exception("❌ No valid JSON found from Claude")

    try:
        return json.loads(json_text)
    except Exception as e:
        raise Exception(f"❌ JSON parsing failed: {str(e)}")