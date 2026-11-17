# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/hello")
# def say_hello():
#     return {"message": "你好,成都!这是我的第一个Web接口!"}


# @app.get("/chat")
# def chat(question: str):
#     answer = f"你问的是：{question},AI正在思考中..."
#     return {"reply": answer}

from fastapi import FastAPI

app = FastAPI()


def my_old_function(question):
    if question == "你好":
        return "你好呀,我是AI小助手。"
    elif question == "几点了":
        return "我也不知道几点了。"
    else:
        return "我不懂你在说什么。"


# 套一个Web的壳子
@app.get("/old_chat")
def chat(question: str):
    result = my_old_function(question)

    # 最后把它用字典装起来发出去
    return {"reply": result}
