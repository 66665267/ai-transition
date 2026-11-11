# age = 20
# if age >= 18:
#     print("你已成年了，可以考驾照了")

# age = 20
# if age >= 18:
#     print("你已经成年了，可以考驾照")
# else:
#     print("你还未成年，不能考驾照。")

# score = 91
# if score >= 90:
#     print("优秀！")
# elif score >= 70:
#     print("良好，继续加油。")
# elif score >= 60:
#     print("及格，争取下次考高点。")
# else:
#     print("不及格，要补考了。")

# password = "123456" # 这是赋值

# # 判断你输入的密码是不是 "123456"
# if password == "123456":
#     print("密码正确，登录成功！")


age = int(input("请输入你的年龄："))
if age < 12:
    print("儿童票，免费")
elif 12 <= age < 60:
    print("成人票,全价100元")
else:
    print("老年票,半价50元")
