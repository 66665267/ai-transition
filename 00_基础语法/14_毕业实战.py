balance = 100.0
while True:
    user_chat = input("请输入(输入q退出): ")
    if user_chat == "q":
        print("退出程序")
        break
    # 2. 如果输入为空（或者全是空格），提示重新输入，不扣费
    if user_chat.strip() == "":
        print("输入不能为空!")
        continue
    if balance >= 3.5:
        balance -= 3.5
        print(f"对话成功,扣费3.5元。当前余额：{balance:.2f}元")
    else:
        print("余额不足，请充值!")
        break
