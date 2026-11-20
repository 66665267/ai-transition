from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()
API_KEY = "e5abc6a37ff2464b6612783cfe072b95.HQGdHAC9Klj0cQsn"


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat_with_ai(req: ChatRequest):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "glm-4-flash",
        "messages": [
            {
                "role": "system",
                "content": "你叫张哥,是个在工地上干了20年的包工头。你脾气极差,说话基本靠吼,极其缺乏耐心,最讨厌别人跟你讲废话。而且你只听得懂四川话。",
            },
            {"role": "user", "content": req.question},
        ],
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    if "choices" not in result:
        print("\n===== 警报！大模型返回了错误信息 =====")
        print(result)  # 👈 这里一定会打印出真实原因
        print("======================================\n")
        return {"answer": "发生错误，请查看终端！"}
    ai_reply = result["choices"][0]["message"]["content"]
    return {"answer": ai_reply}
