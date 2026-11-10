print("--- 练习 1:创建和访问字典 ---")
user = {"name": "江流儿", "age": 37, "city": "成都", "skills": ["Python", "FastAPI"]}
print(f"用户姓名: {user['name']}")
print(f"用户年龄: {user['age']}")
print(f"用户技能: {user['skills']}")
user["age"] = 38
user["is_student"] = True
print(f"修改后的字典: {user}")

print("\n--- 练习 2:遍历字典 ---")
for key, value in user.items():
    print(f"属性名：{key},->属性值: {value}")

print("\n--- 练习 3:字典和JSON互转 ---")
import json

my_dict = {"name": "江流儿", "age": 37, "city": "成都"}
json_str = json.dumps(my_dict, ensure_ascii=False)
print(f"转成JSON长这样:{json_str}")
print(f"他的类型是:{type(json_str)}")
server_response = '{"status":"success","message":"你好,我是AI"}'
dict_data = json.loads(server_response)
print(f"转回字典长这样:{dict_data}")
print(f"他的类型是:{type(dict_data)}")
print(f"我提取里面的 message:{dict_data['message']}")


print("\n--- 练习 4:读取本地文件 ---")
with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"文件里的内容是：\n{content}")
