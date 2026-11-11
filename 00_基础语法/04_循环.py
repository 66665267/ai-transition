# skills = ["Python", "FastAPI", "RAG", "大模型"]
# for skill in skills:
#     print(f"我要学习：{skill}")

# for i in range(3):
#     print(f"这是第{i+1}次循环")

# count = 3
# while count > 0:
#     print(f"倒计时：{count}")
#     count = count - 1
# print("点火，发射！")

# for i in range(1, 6):
#     if i == 3:
#         break
#     print(f"现在的数字是：{i}")
# print("循环结束了！")


password = "123456"
count = 3
while count > 0:
    user_pass = input("请输入密码：")
    if user_pass == password:
        print("登陆成功！")
        break
    else:
        count -= 1
        print(f"密码错误，你还有{count}次机会")
if count == 0:
    print("账号已锁定，请联系客服。")
