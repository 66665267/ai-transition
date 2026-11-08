# for i in range(3):
#     num = int(input("请输入一个数字："))
#     if num > 10:
#         print("大")
#     else:
#         print("小")

name = "江流儿"
age = 37
hobby = "lol"
print(hobby)

if age > 35:
    print("资深职场人")
else:
    print("年轻有为")

for i in range(5):
    print("我一定能转行成功")


def make_juice(fruit):
    result = f"这是一杯新鲜的{fruit}汁"
    return result


my_drink = make_juice("苹果")
print(my_drink)

scores = [80, 90, 70]
total = 0
# 请用 for 循环，把 scores 里的分数加到 total 里面
for score in scores:
    total = total + score
print(f"总分是：{total}")


# 请定义一个函数 check_num，接收一个数字参数 num
# 如果 num 大于 10，返回 "大"，否则返回 "小"
def check_num(num):
    if num > 10:
        return "大"
    else:
        return "小"


result = check_num(15)
print(result)  # 这里应该打印出 "大"

# 有一个字典存着用户信息
user = {"name": "江流儿", "age": 36, "city": "成都"}
for value in user.values():
    print(value)
user = {"name": "江流儿", "age": 36, "city": "成都"}

# .items() 会把字典拆成一对一对的 (key, value)
for key, value in user.items():
    print(f"{key} 是 {value}")
