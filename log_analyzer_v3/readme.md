📊 日志分析工具（Part 3）
一个命令行日志分析工具，用于统计 ERROR/WARNING 日志，并可选校验 JSON 括号合法性。
本项目是 LeetCode「有效括号」问题（Part 2）的实际应用：用你写的括号校验函数，检查日志中 JSON 片段是否格式正确！
✨ 功能亮点
✅ 自动解析日志行（支持 module:xxx, code:xxx, msg:xxx 格式）
✅ 按模块（如 auth, payment）统计 ERROR 或 WARNING 数量
✅ 可选开启 JSON 括号校验（复用 Part 2 的算法）
✅ 输出结构化报告（report.json），便于后续处理
✅ 简洁易用的命令行接口（CLI）
📁 项目结构
text

编辑



log_analyzer_v3/
├── log_analyzer.py    # 主程序
├── test.log           # 示例日志文件（可自定义）
├── report.json        # 分析结果输出（自动生成）
└── README.md          # 本说明文件
🚀 快速开始
1. 准备日志文件
创建一个日志文件（例如 test.log），格式如下：
log

编辑



2025-02-27 10:00:01 ERROR module:auth ip:192.168.1.1 code:E1001 msg:{"user":"alice"}
2025-02-27 10:00:02 WARNING module:cache ip:10.0.0.5 code:W2003 msg:Cache miss
2025-02-27 10:00:03 ERROR module:payment ip:192.168.1.2 code:E2005 msg:{"amount":100
💡 注意：第3行故意缺少 }，用于测试 JSON 校验功能。
2. 运行分析
在终端中执行以下命令：
基础分析（仅统计 ERROR）：
bash

编辑



python log_analyzer.py --input test.log
启用 JSON 括号校验：
bash

编辑



python log_analyzer.py --input test.log --check-json
3. 查看结果
分析完成后，结果会自动保存到 report.json，例如：
json

编辑



{
  "auth": {
    "count": 1,
    "codes": ["E1001"],
    "bad_json_lines": []
  },
  "payment": {
    "count": 1,
    "codes": ["E2005"],
    "bad_json_lines": [3]
  }
}
字段说明：
count：该模块的错误总数
codes：所有出现的错误码
bad_json_lines：JSON 括号不合法的行号（仅当启用 --check-json 时存在）
🛠️ 命令行参数说明
表格
参数	是否必需	说明
--input 或 -i	✅ 是	输入日志文件路径（如 app.log）
--check-json	❌ 否	开启 JSON 括号合法性校验
💡 使用 python log_analyzer.py --help 查看帮助信息。
🔧 技术细节
括号校验：复用 Part 2 的栈（stack）算法，仅校验 ()[]{}。
日志格式要求：
第3个字段必须是 ERROR 或 WARNING
必须包含 module:xxx 和 code:xxx
其他字段（如 ip, msg）可选
编码：默认使用 UTF-8 读取日志
🎯 学习目标达成
通过本项目，你已掌握：
✅ 将算法（有效括号）应用于实际场景
✅ 解析结构化文本日志
✅ 构建命令行工具（CLI）
✅ 生成结构化输出（JSON 报告）
