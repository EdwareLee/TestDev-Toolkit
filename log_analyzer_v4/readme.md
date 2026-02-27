

# Log Analyzer

轻量级日志分析工具，专为测试开发设计。自动解析日志中的模块、IP 和错误码，支持异常容错。

## ✨ 功能
- 自动识别 `ERROR` / `WARNING`
- 提取 `module`、客户端 `IP`、错误码（如 `(code: E1001)`）
- 文件不存在、编码错误、脏数据等场景**不崩溃**
- 返回结构化统计结果

## 🚀 使用
```python
from log_analyzer import analyze_log

result = analyze_log("app.log")
print(result)
```
输出示例：
```
{
  "login": {"count": 1, "ips": ["192.168.1.1"], "errors": ["E1001"]},
  "payment": {"count": 1, "ips": [], "errors": []}
}
```
🧪 测试
```bash
pip install pytest
pytest -v
```
包含 5 个测试用例，覆盖正常与异常场景。

📦 依赖

Python 3.7+
无第三方依赖（仅用标准库）