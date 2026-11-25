from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()
API_KEY = "e5abc6a37ff2464b6612783cfe072b95.HQGdHAC9Klj0cQsn"


# 1. 接收前端传来的文本
class TicketRequest(BaseModel):
    text: str


@app.post("/classify")
def classify_ticket(ticket: TicketRequest):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    # 🌟 核心：给大模型下达死命令，不让它废话
    prompt = f"""
    你是一个客服分类助手。请判断以下用户投诉属于哪种类型。
    你只能回答以下三个词中的一个，绝对不能包含其他任何标点符号或废话：
    退款
    技术问题
    其他
    
    用户投诉：{ticket.text}
    """

    data = {"model": "glm-4-flash", "messages": [{"role": "user", "content": prompt}]}

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    # 拿到大模型的判断结果，并且去掉可能存在的空格
    ai_reply = result["choices"][0]["message"]["content"].strip()

    # ==========================================
    # 👇 下面轮到你的纯逻辑出场了！（结合Day 3的if）
    # ==========================================

    if ai_reply == "退款":
        msg = "已为您自动转接财务客服。"
    elif ai_reply == "技术问题":
        msg = "已提交给技术团队，请稍候。"
    else:
        msg = "已记录您的问题，请耐心等待。"

    return {"大模型的分类": ai_reply, "系统回复": msg}
