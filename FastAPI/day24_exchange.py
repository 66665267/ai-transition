from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 这是咱们的“小数据库”，用字典存用户的积分
users_db = {"张飞": 100, "关羽": 50}


# 接收前端发来的请求：谁，想兑换多少积分的商品
class ExchangeRequest(BaseModel):
    user_name: str
    item_price: int


@app.post("/exchange")
def exchange_item(req: ExchangeRequest):

    # =========================================
    # 👇 从这里开始，你自己写逻辑（用昨天学的 if...else）
    # =========================================

    # 1. 先判断，这个人到底在不在咱们的数据库里（提示：用 in 关键字）
    if req.user_name in users_db:
        # 2. 如果在，再判断他的积分够不够（提示：用字典取值，和商品价格比较）
        if users_db[req.user_name] >= req.item_price:
            # 3. 如果够，扣积分！(把数据库里的积分减去商品价格)
            users_db[req.user_name] = users_db[req.user_name] - req.item_price
            return {
                "status": "success",
                "msg": f"{req.user_name} 兑换成功！剩余积分：{users_db[req.user_name]}",
            }
        else:
            # 4. 如果不够，返回失败
            return {"status": "error", "msg": "积分不足，无法兑换！"}
    else:
        # 5. 如果根本不在数据库里
        return {"status": "error", "msg": "查无此人！"}

    return {"status": "success"}  # 占位符，不用管
