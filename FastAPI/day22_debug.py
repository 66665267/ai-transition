from fastapi import FastAPI
from pydantic import BaseModel  # 这里没问题

app = FastAPI()


class UserInfo(BaseModel):  # 👈 Bug 1 藏在这里
    name: str
    phone: str


@app.post("/hide_phone")
def hide_phone(info: UserInfo):
    phone_num = info.phone

    # 如果手机号是11位，就脱敏
    if len(phone_num) == 11:
        new_phone = phone_num.replace(phone_num[3:7], "****")  # 👈 Bug 2 藏在这里
        return {"status": "success", "phone": new_phone}
    else:
        return {"status": "error", "msg": "手机号格式不对"}  # 👈 Bug 3 藏在这里
