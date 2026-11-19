from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()
# 填你昨天注册的智谱 API Key
API_KEY = "e5abc6a37ff2464b6612783cfe072b95.HQGdHAC9Klj0cQsn"


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat_with_ai(req: ChatRequest):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    # 把用户传过来的问题塞给大模型
    data = {
        "model": "glm-4-flash",
        "messages": [
            {
                "role": "system",
                "content": "你叫王老五,是成都一家开了20年苍蝇火锅店的老板。你说话必须带四川口音(比如：巴适、瓜娃子、晓得、安逸），极其热情,而且三句话离不开推销你的毛肚和鸭肠。绝对不要像机器人一样回答。",
            },
            {"role": "user", "content": req.question},
        ],
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    ai_reply = result["choices"][0]["message"]["content"]
    return {"answer": ai_reply}
