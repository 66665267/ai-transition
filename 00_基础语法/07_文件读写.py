# 1. 写文件（'w' 代表覆盖写入）
with open("text.txt", "w", encoding="utf-8") as f:
    f.write("您好,这是我用Python写的第一行字。\n")
    f.write("第二行：转行之路，关关难过关关过！\n")
# 2.读文件（'r'代表读取）
with open("text.txt", "r", encoding="utf-8") as f:
    content = f.read()  # 把里面的内容全读出来
    print("---读取到的内容如下---")
    print(content)

import json  # 必须导入这个工具箱才能处理json

my_data = {"name": "江流儿", "target": "AI应用工程师", "skills": ["Python", "FastAPI"]}
# 2.把字典写入user.json文件
with open("user.json", "w", encoding="utf-8") as f:
    # indent=4是为了让文件排版好看，ensure_ascii=False是为了显示中文
    json.dump(my_data, f, ensure_ascii=False, indent=4)
# 3.从user.json 文件读取出来，变回字典
with open("user.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print("\n---从JSON读出来的名字---")
print(loaded_data["name"])  # 看，读出来之后，又要能像字典一样提取了！
