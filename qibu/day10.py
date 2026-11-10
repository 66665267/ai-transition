import requests

# 🚨 你的钥匙就填在下面引号里！把里面的字换成你刚才复制的长串字母
API_KEY = "e5abc6a37ff2464b6612783cfe072b95.HQGdHAC9Klj0cQsn"

url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
data = {
    "model": "glm-4-flash",
    "messages": [
        {
            "role": "user",
            "content": "请用一句话鼓励一下37岁正在成都转行学Python的大龄青年。",
        }
    ],
}

print("AI 正在思考中，请稍候...")

response = requests.post(url, headers=headers, json=data)
result = response.json()

ai_reply = result["choices"][0]["message"]["content"]

print("\n--- AI 的回复 ---")
print(ai_reply)
