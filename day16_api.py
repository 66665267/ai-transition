from fastapi import FastAPI

app = FastAPI()


@app.get("/discount")
def calculate_discount(username: str, amount: float):
    final_price = amount
    if username == "vip":
        final_price = amount * 0.8
    elif username == "normal":
        final_price = amount * 0.9
    else:
        print("普通用户无折扣")
    return {"用户名": username, "原始金额": amount, "最终需要支付": final_price}
