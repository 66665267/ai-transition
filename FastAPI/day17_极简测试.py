from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 1. 这是咱们画的“收件单”，规定前端必须传 name(名字) 和 age(年龄)
class UserInfo(BaseModel):
    name: str
    age: int


# 2. 开门营业，注意这是 POST（接收纸条）
@app.post("/register")
def register(user: UserInfo):
    # 3. 把纸条里接收到的年龄，用你 Day 3 学的 if...else 做判断
    if user.age >= 18:
        return {"msg": f"你好 {user.name}，你成年了，注册成功！"}
    else:
        return {"msg": f"你好 {user.name}，未成年不能注册。"}
