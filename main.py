import os, requests

api_key=os.environ["OPENROUTER_API_KEY"]
webhook=os.environ["DISCORD_WEBHOOK_URL"]

prompt="""Generate one original creative writing prompt.
Include:
- A creative title
- 150-250 word prompt
- Suitable for a Discord writing community.
Return plain text only."""

resp=requests.post(
 "https://openrouter.ai/api/v1/chat/completions",
 headers={
   "Authorization":f"Bearer {api_key}",
   "Content-Type":"application/json"
 },
 json={
   "model":"meta-llama/llama-3.3-8b-instruct:free",
   "messages":[{"role":"user","content":prompt}]
 }
)
resp.raise_for_status()
text=resp.json()["choices"][0]["message"]["content"]

requests.post(webhook,json={"content":"# ✍️ Daily Writing Prompt\n\n"+text}).raise_for_status()
print("Posted successfully")
