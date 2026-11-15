# users=["张飞","关羽"]
# if "张飞"in users:
#     print("张飞已经在列表里了!")

user_list = []
while True:  # True 代表一直循环
    username = input("请输入你的用户名(输入q退出):")
    if username == "q":
        print("退出系统。")
        break
    if username.strip() == "":
        print("用户名不能为空，请重新输入!")
        continue
    if username.strip() in user_list:
        print("该用户已被注册，请换一个")
    else:
        user_list.append(username.strip())
        print(f"注册成功！当前系统里的用户有：{user_list}")

print(f"\n最终系统留里的用户:{user_list}")
