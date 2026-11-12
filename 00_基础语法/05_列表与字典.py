# fruits = ["苹果", "香蕉", "橘子"]
# fruits.append("西瓜")
# print(f"增加后：{fruits}")
# fruits.remove("香蕉")
# print(f"删除后：{fruits}")
# fruits[0] = "大苹果"
# print(f"修改后：{fruits}")
# print(f"现在有{len(fruits)}种水果")

# user = {"name": "江流儿", "age": 37, "city": "成都"}
# print(f"提取名字：{user['name']}")
# user["age"] = 38
# print(f"修改年龄后：{user}")
# user["job"] = "AI应用工程师"
# print(f"增加职业后：{user}")

cart = []
item1 = {"name": "键盘", "price": 199}
item2 = {"name": "鼠标", "price": 99}
cart.append(item1)
cart.append(item2)
print(f"购物车里的全部数据：{cart}")
for item in cart:
    print(f"商品：{item['name']},价格：{item['price']}元")
