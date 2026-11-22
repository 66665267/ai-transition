from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 1. 规定前端传过来的格式：必须有一篇文章
class Article(BaseModel):
    text: str


# 2. 开一个门牌号叫 /count (统计的意思)
@app.post("/count")
def count_article(article: Article):
    # 思路 1：把前端发来的文章内容，提取出来
    wenzhang = article.text
    # 思路 2：算总字数 (用 len() 函数)
    zongzishu = len(wenzhang)
    # 思路 3：算总词数 (用 split() 把文章按空格切成列表，然后再算列表的长度)
    cibiao = wenzhang.split()

    zongcishu = len(cibiao)
    first = cibiao[0]
    # 思路 4：打包结果返回
    return {
        "状态": "成功",
        "文章总字数": zongzishu,
        "文章总词数": zongcishu,
        "第一篇词是什么": first,
    }
