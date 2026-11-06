print("--- 练习 1 : 遍历列表 ---")
skills = ["python", "FastAPI", "RAG", "Agent", "Docker"]
for skill in skills:
    print(f"我要学习：{skill}")
    print("-------------")
print("\n--- 练习 2:for 结合 range ---")
for i in range(1, 6):
    print(f"今天是学习Python的第{i}天")
print("\n--- 练习 3:密码验证(最多试三次) ---")
password = "66665267"
attempts = 3
while attempts > 0:
    user_input = input("请输入密码：")
    if user_input == password:
        print("密码正确，登录成功")
        break
    else:
        attempts = attempts - 1
        print(f"密码错误，你还有{attempts}次机会。")

if attempts == 0:
    print("次数耗尽，账号已锁定。")
print("\n--- 练习 4: 筛选出及格的分数 ---")
scores = [95, 45, 78, 88, 59, 62, 30, 99]
for score in scores:
    if score >= 60:
        print(f"分数{score}:及格!")
    else:
        print(f"分数{score}:不及格，需要重考。")
