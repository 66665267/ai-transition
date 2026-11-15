# 想象这是一个大模型发给你的标准数据
data = {
    "model": "glm-4-flash",
    "usage": {"total_tokens": 57},
    "choices": [{"content": "你好,我是AI助手!"}],
}
# 第一关：拿外面的数据，很简单
print(data["model"])  # 打印出 glm-4-flash
# 第二关：拿里面的数据（字典套字典）
# 逻辑：先找 usage，再找 total_tokens
print(data["usage"]["total_tokens"])  # 打印出 57
# 第三关：拿列表里的数据（字典套列表套字典）
# 逻辑：先找 choices 拿列表，拿第 0 个，再拿 content
print(data["choices"][0]["content"])  # 打印出 你好，我是AI助手！
