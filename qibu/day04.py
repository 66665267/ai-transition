# print("--- 练习 1:最简单的函数 ---")


# def say_hello():
#     print("您好,未来的AI应用工程师")
#     print("今天也要努力敲代码哦")


# say_hello()
# say_hello()

# print("\n--- 练习 2: 带参数的函数 ---")


# def check_score(score):
#     if score >= 60:
#         print(f"得分{score},及格了！")
#     else:
#         print(f"得分{score},不及格！")


# check_score(85)
# check_score(45)

# print("\n--- 练习 3: 带返回值的函数 ---")


# def add_numbers(a, b):
#     result = a + b
#     return result


# my_sum = add_numbers(10, 20)
# print(f"10 + 20 的结果是： {my_sum}")
# print(f"5 + 5 的结果是:{add_numbers(5,5)}")


# register_user = "用户名:江流儿,密码:123456"
# denglu_user = input("请输入您的用户名:")
# denglu_pass = input("请输入您的密码:")
# print("注册成功")


# attempts = 3
# while attempts > 0:
#     denglu_user = input("请输入用户名：")
#     denglu_pass = input("请输入密码：")
#     if denglu_user == "江流儿" and denglu_pass == "123456":
#         print("登录成功")
#         break
#     else:
#         attempts = attempts - 1
#         print(f"用户名或密码错误，你还有{attempts}次机会。")
# if attempts == 0:
#     print("账号已锁定")


def register():
    print("--- 注册系统 ---")
    user = "江流儿"
    pwd = "123456"
    print(f"注册成功,您的账号是:{user},请牢记密码。")
    return user, pwd


def login(saved_user, saved_pwd):
    print("\n--- 登录系统 ---")
    attempts = 3
    while attempts > 0:
        input_user = input("请输入用户名：")
        input_pwd = input("请输入密码：")
        if input_user == saved_user and input_pwd == saved_pwd:
            print("登录成功,欢迎进入系统！")
            break
        else:
            attempts -= 1
            print(f"用户名或密码错误，你还有{attempts}次机会。")
    if attempts == 0:
        print("账号已锁定!")


saved_username, saved_password = register()
login(saved_username, saved_password)

login("江流儿", "123456")
