from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests

app = FastAPI()
API_KEY = "e5abc6a37ff2464b6612783cfe072b95.HQGdHAC9Klj0cQsn"


# 1. 规定前端必须传过来一个 JSON，里面包含 question
class ChatRequest(BaseModel):
    question: str


# 2. 注意这里是 @app.post，不再是 get 了
@app.post("/chat")
def chat_with_ai(req: ChatRequest):
    print(f"🔥【前端发来的问题】：{req.question}")
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "glm-4-flash",
        "messages": [
            {
                "role": "user",
                "content": f"你现在是一个非常傲娇的猫娘，请用这种语气回答我：{req.question}",
            }
        ],  # 这里用 req.question 接收
    }
    print(f"📦【即将发给大模型的完整数据】：{data}")
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    print("大模型返回的结果是：", result)
    ai_reply = result["choices"][0]["message"]["content"]
    return {"answer": ai_reply}


# 3. 当别人访问首页时，把网页文件发给他
@app.get("/")
def read_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read(), status_code=200)
