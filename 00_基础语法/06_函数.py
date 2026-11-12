# def say_hello():
#     print("你好，江流儿！")
#     print("欢迎来到AI世界!")

# say_hello()

# def make_juice(fruit):
#     print(f"正在榨{fruit}汁...")
#     print("叮!榨好了!")


# make_juice("苹果")
# make_juice("西瓜")
# def add_numbers(a, b):
#     result = a + b
#     return result


# my_sum = add_numbers(10, 20)
# print(f"算出来的结果是：{my_sum}")

cart = []
item1 = {"name": "键盘", "price": 199}
item2 = {"name": "鼠标", "price": 99}
cart.append(item1)
cart.append(item2)


def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"]
    return total


final_price = calculate_total(cart)
print(f"总价是：{final_price}元")
