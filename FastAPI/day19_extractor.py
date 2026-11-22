from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

app = FastAPI()
API_KEY = "e5abc6a37ff2464b6612783cfe072b95.HQGdHAC9Klj0cQsn"


class ShouJianXinFeng(BaseModel):
    text: str


@app.post("/tiqu")
def ti_qu_xin_xi(qing_qiu: ShouJianXinFeng):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    nao_dai = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    gei_da_mo_xing_de_hua = f"请提取以下信息,返回JSON:{qing_qiu.text}"
    ji_chu_qu_de_bao_guo = {
        "model": "glm-4-flash",
        "messages": [{"role": "user", "content": gei_da_mo_xing_de_hua}],
    }
    qian_shou = requests.post(url, headers=nao_dai, json=ji_chu_qu_de_bao_guo)
    jie_guo = qian_shou.json()
    ai_de_hui_da = jie_guo["choices"][0]["message"]["content"]
    ai_de_hui_da = ai_de_hui_da.replace("```json", "").replace("```", "").strip()
    try:
        zui_zhong_shu_ju = json.loads(ai_de_hui_da)
        return {"zhuang_tai": "cheng_gong", "shu_ju": zui_zhong_shu_ju}
    except:
        return {"zhuang_tai": "shi_bai", "yuan_yin": "AI乱说话"}
