# 🛠️ TestDev-Toolkit — 测试开发工程师的自动化工具箱

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Code Size](https://img.shields.io/github/languages/code-size/EdwareLee/TestDev-Toolkit)]()


这是一个为**测试工程师**打造的轻量级 CLI 工具集合，旨在解决日常工作中重复、低效、易错的手动操作。所有工具均支持命令行调用，自带示例与单元测试，可直接集成到你的质量保障流程中。


---

## ✨ 核心能力

| 工具 | 功能 | 解决痛点 |
|------|------|--------|
| **`log_analyzer`** | 流式解析 GB 级日志，提取错误/IP/模块 | 告别 `grep` + `awk` 手动排查 |
| **`api_tester`** | 自动生成合规数据 → 发送请求 → 深度校验响应结构 | 接口测试覆盖不全、校验不严 |
| **`config_validator`** | 校验 JSON/YAML 语法 + 必填字段 + 类型 | 配置缩进错误导致部署失败 |
| **`perf_analyzer`** | 分析 API 延迟日志，检测 P99 突增，生成健康报告 | 性能问题发现滞后、无趋势洞察 |

---

## ▶️ 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/EdwareLee/TestDev-Toolkit.git
cd TestDev-Toolkit
```
### 2. 安装依赖（可选，仅 yaml 需额外安装）
```bash

pip install pyyaml  # 用于 config_validator
```

### 3. 运行任意工具（无需安装，直接调用模块）
```
python -m src.log_analyzer.cli --input logs/sample_app.log
```
输出：错误统计、高频IP、模块分布

### ⚙️ 配置校验示例
```bash
python -m src.config_validator \
  --config config/app.yaml \
  --required host,port \
  --types port:int,debug:bool
```
输出：✅ Valid 或 ❌ Invalid + 错误详情
### 📈 性能报告生成示例
```bash

python -m src.perf_analyzer \
  --input perf/perf.log \
  --output report.md \
  --window minute
```
### 输出：report.md（含健康评分、告警建议、趋势摘要）
### 🧪 单元测试
所有模块均通过 pytest 覆盖核心逻辑：
```bash

pytest tests/ -v
```
### 测试用例包括：
* 正常路径（合法日志、有效配置）
* 边界条件（空文件、单行日志）
* 异常场景（非法JSON、缺失字段、类型错误）

---
### 📂 项目结构
```
TestDev-Toolkit/
├── src/                    # 源代码
│   ├── log_analyzer/       # 日志分析器
│   ├── api_tester/         # API 测试套件
│   ├── config_validator/   # 配置校验器
│   └── perf_analyzer/      # 性能分析器
├── logs/                   # 示例日志
├── config/                 # 示例配置 (JSON/YAML)
├── perf/                   # 示例性能日志
├── tests/                  # 单元测试
├── LICENSE
└── README.md
```

### 💼 为什么这个项目有价值？
* 真实场景驱动：每个工具都源于测试工程师的日常痛点；
* 生产就绪设计：支持大文件、异常降级、清晰错误提示；
* 工程规范：模块化、CLI 友好、测试覆盖、文档齐全；
* 可扩展性强：轻松接入新日志格式、新校验规则、新报告模板。
