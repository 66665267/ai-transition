from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello AI 工程师！这是我写的第一个接口！"}
