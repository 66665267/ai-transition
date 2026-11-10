from fastapi import FastAPI
import requests

app = FastAPI()
API_KEY = "e5abc6a37ff2464b6612783cfe072b95.HQGdHAC9Klj0cQsn"


@app.get("/chat")
def chat_with_ai(question: str):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"model": "glm-4-flash", "messages": [{"role": "user", "content": question}]}

    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    ai_reply = result["choices"][0]["message"]["content"]

    return {"你的问题": question, "AI的回答": ai_reply}
