# # 用户输入文字，我们硬是把它当数字算
# user_input = "我是文字不是数字"
# num = int(user_input)  # 这一步会瞬间崩溃！
# print("这句话永远不会被打印出来。")

# user_input = "我是文字"
# try:
#     # 尝试执行这里面的代码
#     num = int(user_input)
#     print(f"转换成功，数字是{num}")
# except:
#     # 如果try里面的代码报错了，立刻跳到这里执行
#     print("哎呀，你输入的不是数字，转换失败了，但程序没有崩溃！")
# print("程序继续安全地往下执行...")

# try:
#     # 故意除以零
#     result = 10 / 0
# except ZeroDivisionError:
#     print("数学老师说过,0不能做除数!")
# except Exception as e:
#     # 兜底方案：捕获其他所有未知错误，并打印出错误原因
#     print(f"发生了一个未知错误{e}")

try:
    user_age = int(input("请输入你的年龄："))
    if user_age < 12:
        print("免费")
    elif 12 <= user_age < 60:
        print("全价100")
    else:
        print("半价50")
except ValueError:
    print("你输入的不是数字，请重新运行！")
except Exception as e:
    print(f"发生了一个未知错误：{e}")
print("程序运行结束")
