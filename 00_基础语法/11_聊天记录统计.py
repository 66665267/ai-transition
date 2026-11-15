# 把这段数据复制到你的代码里
chat_history = [
    {"user": "江流儿", "content": "你好,请问AI怎么转行?"},
    {"user": "AI助手", "content": "你好!转行AI建议先从Python基础学起。"},
    {"user": "江流儿", "content": "那学完基础之后呢？我想在成都找工作。"},
    {
        "user": "AI助手",
        "content": "学完基础可以尝试做RAG知识库项目,这是目前企业最需要的。",
    },
]
# 记录总句数
total_count = 0
# 记录最长的那句话（先设为空）
longest_message = ""
longest_user = ""

for chat in chat_history:
    # 每循环一次，说明有一句话，总数加1
    total_count += 1
    # 提取这句话是谁说的，内容是什么（剥洋葱）
    user = chat["user"]
    content = chat["content"]
# 如果当前这句话的字数，大于最长记录的字数
if len(content) > len(longest_message):
    # 就把当前的内容和用户名，替换掉旧的记录
    longest_message = content
    longest_user = user
print(f"一共聊了 {total_count} 句话。")
print(f"最长的一句话是 {longest_user} 说的，内容是：{longest_message}")
