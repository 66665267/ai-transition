import json  # 差点忘了这个，必须有！

# 建一个字典列表
cart = [{"name": "键盘", "price": 199}, {"name": "鼠标", "price": 99}]
# 把这个cart写进cart.json
with open("cart.json", "w", encoding="utf-8") as f:
    json.dump(cart, f, ensure_ascii=False, indent=4)


#  定义一个函数，用来计算总价（把求和逻辑放进来）
def calculate_total(data):
    total = 0
    for i in data:
        total += i["price"]
    return total


# 再从 cart.json 里把它读出来，存进一个变量。
with open("cart.json", "r", encoding="utf-8") as f:
    data = json.load(f)
final_price = calculate_total(data)
print(f"购物车总价是：{final_price}元")
