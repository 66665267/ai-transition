# # 1.造一个叫Dog的模具
# class Dog:
#     # 2.初始化方法，每次捏狗的时候，必须给名字和年龄
#     def __init__(self, name, age):
#         self.name = name  # 把名字绑在这只狗身上
#         self.age = age  # 把年龄绑在这只狗身上

#     # 3.定义一个方法（就是狗的技能）
#     def bark(self):
#         print(f"我叫{self.name},今年{self.age}岁，汪汪汪！")


# # 4.用模具捏两只狗(创建对象)
# dog1 = Dog("旺财", 3)
# dog2 = Dog("来福", 5)
# # 5.让他们叫
# dog1.bark()
# dog2.bark()


# 1.造一个叫User的模具
class User:
    # 2.初始化方法，每次接收必须给名字和角色
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        print(f"我的名字是{self.name},我的系统角色是{self.role}")


user1 = User("江流儿", "超级VIP")
user2 = User("张飞", "普通用户")
user1.introduce()
user2.introduce()
