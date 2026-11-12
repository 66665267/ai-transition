print("--- 练习1:买票判断 ---")
age = 20
if age >= 18:
    print("成年人，需要买全票。")
else:
    print("未成年，可以买半票。")

print("\n---- 练习2:成绩判断 ---")
score = 85
if score >= 90:
    print("优秀！")
elif score >= 70:
    print("良好，继续加油。")
elif score >= 60:
    print("及格，争取下次考高点。")
else:
    print("不及格，需要补考。")

print("\n---- 练习3:人机互动 ---")
your_age = input("请输入你的年龄：")
if int(your_age) >= 35:
    print("资深职场人,AI转型正当时!")
else:
    print("年轻就是资本,AI等着你!")
