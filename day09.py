from fastapi import FastAPI

app = FastAPI()


@app.get("/greet/{username}")
def ask_ai(username: str):
    return {"message": f"您好,{username}!欢迎来到成都AI开发圈。"}


@app.get("/add")
def add_numbers(a: int, b: int):
    result = a + b
    return {"result": result}
