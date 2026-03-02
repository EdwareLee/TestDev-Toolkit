import requests
import json

url = 'https://httpbin.org/json'
resp = requests.get(url)

if resp.status_code == 200:
    try:
        data = resp.json()
        # 美化打印：缩进4个空格，中文不转义（ensure_ascii=False）
        print("✅ 成功解析 JSON:")
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except requests.exceptions.JSONDecodeError:
        print("❌ 不是 JSON，内容为：", resp.text[:300])