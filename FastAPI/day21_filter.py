# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# # 定义接收前端文本的格式
# class UserText(BaseModel):
#     text: str


# @app.post("/filter")
# def filter_text(user_text: UserText):
#     heimingdan = ["垃圾", "骗子", "傻瓜"]
#     wenzhang = user_text.text
#     for ci in heimingdan:
#         wenzhang = wenzhang.replace(ci, "***")
#     return {"状态": "过滤完成", "处理后的文本": wenzhang}
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 1. 规定前端发来的格式（照抄之前一样的套路）
class MiMa(BaseModel):
    text: str


@app.post("/hide")
def hide_mima(mima: MiMa):
    # 2. 拿到原文
    yuan_wen = mima.text

    # 3. 准备要替换的“子弹”
    shu_zi = "0123456789"
    zi_mu = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # 4. 👇 从这里开始，你自己写！
    # 提示：你要遍历 shu_zi 和 zi_mu，把 yuan_wen 里的它们换掉。
    # 你可以用两个 for 循环，也可以用今天抄的那个逻辑。

    for c in shu_zi:
        # 填空：用 yuan_wen 把它替换掉
        yuan_wen = yuan_wen.replace(c, "*")

    for c in zi_mu:
        # 填空：用 yuan_wen 把它替换掉
        yuan_wen = yuan_wen.replace(c, "*")

    # 5. 返回结果
    return {"脱敏后的密码": yuan_wen}
