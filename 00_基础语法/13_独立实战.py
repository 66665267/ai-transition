# 1. 准备数据 (token_records)
token_records = [150, 80, 320, 45, 600, 120]
# 2. 准备一个变量装总 Token 数，初始为 0
total_token = 0
# 3. 准备一个变量装最高 Token 数，初始为 0
max_token = 0
# 4. 用 for 循环把列表里的数字挨个拿出来
for count in token_records:
    # 5. 把拿出来的数字加到“总 Token 数”里
    total_token += count
    # 6. 如果拿出来的数字，比“最高 Token 数”还大，就把它的值替换给“最高 Token 数”
    if count > max_token:
        max_token = count
# 7. 循环结束后，打印总 Token 数和最高 Token 数
print(f"总Token数:{total_token}")
print(f"单次最高 Token 数:{max_token}")
