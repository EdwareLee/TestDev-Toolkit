# Test Report Comparator

一个轻量级 Python 工具，用于自动比对两份测试报告中的用例差异，快速识别**缺失用例**和**新增用例**，提升回归测试效率。

> 💡 **核心优势**：基于 `set` 集合操作，O(1) 高效比对，10,000+ 用例秒级分析！

---

## ✨ 功能特点

- ✅ 自动去重（忽略重复用例 ID）
- ✅ 找出两份报告的**共同用例**
- ✅ 标记 **report1 有但 report2 缺失的用例**（可能漏测！）
- ✅ 标记 **report2 新增的用例**（新功能/新覆盖）
- ✅ 支持空行过滤与文件异常处理
- ✅ 输出结构化结果，便于集成到 CI/CD 流程

---

## 🚀 快速使用

### 1. 准备测试报告文件（纯文本，每行一个用例 ID）

`report_old.txt`
TC001
TC002
TC003
`report_new.txt`

TC002
TC003
TC004

### 2. 调用函数

```python
from test_report_comparator import compare_test_reports

result = compare_test_reports("report_old.txt", "report_new.txt")
print(result)
```
3. 输出示例
json

编辑



{
  "common": 2,
  "missing_in_rep2": ["TC001"],
  "new_in_rep2": ["TC004"],
  "total_rep1": 3,
  "total_rep2": 3
}
🛠️ 本地运行测试
bash

编辑



python test_report_comparator.py
（确保同目录下有 report_old.txt 和 report_new.txt）
📌 应用场景
回归测试前后用例覆盖对比
自动化测试结果 vs 手工测试清单校验
持续集成中监控测试范围变化