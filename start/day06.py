# # 1. 准备原始数据（列表里面装字典）
# students = [
#     {"name": "张飞", "score": 85},
#     {"name": "魏延", "score": 88},
#     {"name": "关羽", "score": 75},  # 故意加一个不及格/小于80的，用来测试
#     {"name": "赵云", "score": 92},
# ]

# # 2. 准备一个空列表，用来装筛选出来的名字
# top_students = []

# # 3. 遍历列表里的每一个字典
# for student in students:
#     # 4. 判断：如果这个人的分数大于80
#     if student["score"] > 80:
#         # 5. 提取他的名字，放进新列表里
#         top_students.append(student["name"])

# # 6. 打印最终结果
# print(f"分数大于80的学生有:{top_students}")
import json


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.loads(file.read())


def analyze_scores(students):
    print("--- 成绩分析报告 ---")
    total_score = 0
    highest_scorer = ""
    highest_score = 0
    fail_students = []
    top_students = []
    for student in students:
        name = student["name"]
        score = student["score"]
        total_score += score
        if score > highest_score:
            highest_score = score
            highest_scorer = name
        if score < 60:
            fail_students.append(name)
        if score > 80:
            top_students.append(name)
    average_score = total_score / len(students)
    print(f"班级总人数：{len(students)}人")
    print(f"班级平均分：{average_score:.1f}分")
    print(f"最高分得主：{highest_scorer}({highest_score}分)")
    print(f"不及格名单：{fail_students}")
    print(f"80分以上的优秀学生:{top_students}")


if __name__ == "__main__":
    student_data = load_data("score.json")
    analyze_scores(student_data)
