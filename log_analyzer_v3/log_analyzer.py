#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
日志分析工具 v3
功能：
  - 统计 ERROR/WARNING 日志按模块分布
  - 校验日志中 JSON 片段的括号合法性
"""

import argparse
import json
import sys
from collections import defaultdict


def is_valid_brackets(s: str) -> bool:
    """判断字符串中的括号是否有效（仅处理 ()[]{}）"""
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack


def read_one_log_line(line):
    """从一行日志中提取信息"""
    # 按空格切分成单词
    words = line.strip().split()
    
    # 如果单词太少，跳过
    if len(words) < 6:
        return None
    
    # 第3个单词是日志级别（ERROR / WARNING）
    log_level = words[2]
    if log_level != "ERROR" and log_level != "WARNING":
        return None
    
    # 先设默认值
    module = "unknown"
    code = "unknown"
    msg = ""
    
    # 从第4个单词开始找 key:value
    for word in words[3:]:
        if word.startswith("module:"):
            module = word[7:]      # 去掉 "module:"
        elif word.startswith("code:"):
            code = word[5:]        # 去掉 "code:"
        elif word.startswith("msg:"):
            msg = word[4:]         # 去掉 "msg:"
    
    # 返回整理好的信息
    return {
        "level": log_level,
        "module": module,
        "code": code,
        "msg": msg
    }


def analyze_log_file(file_path: str, target_level: str = "ERROR", check_json: bool = False):
    stats = defaultdict(lambda: {
        "count": 0,
        "ips": set(),
        "codes": set(),
        "invalid_json_lines": []
    })
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            data = parse_log_line(line)
            if not data:
                continue
            
            if data["level"] != target_level:
                continue
            
            mod = data["module"]
            stats[mod]["count"] += 1
            stats[mod]["ips"].add(data["ip"])
            stats[mod]["codes"].add(data["code"])
            
            if check_json:
                if not is_valid_brackets(data["msg"]):
                    stats[mod]["invalid_json_lines"].append(line_num)
    
    result = {}
    for mod, info in stats.items():
        result[mod] = {
            "count": info["count"],
            "ips": list(info["ips"]),
            "codes": list(info["codes"])
        }
        if check_json:
            result[mod]["invalid_json_lines"] = info["invalid_json_lines"]
    
    return result


def main():
    parser = argparse.ArgumentParser(
        description="专业日志分析工具 - 统计 ERROR/WARNING 并支持 JSON 校验",
        prog="log_analyzer"
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="输入日志文件路径 (例如: app.log)"
    )
    parser.add_argument(
        "--output", "-o",
        default="report.json",
        help="输出报告路径 (默认: report.json)"
    )
    parser.add_argument(
        "--level",
        choices=["ERROR", "WARNING"],
        default="ERROR",
        help="要分析的日志级别 (默认: ERROR)"
    )
    parser.add_argument(
        "--check-json",
        action="store_true",
        help="校验日志中 msg 字段的 JSON 括号是否合法"
    )
    
    args = parser.parse_args()
    
    try:
        result = analyze_log_file(
            file_path=args.input,
            target_level=args.level,
            check_json=args.check_json
        )
        
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        total_modules = len(result)
        total_logs = sum(mod["count"] for mod in result.values())
        print(f"✅ 分析完成!")
        print(f"   报告已保存至: {args.output}")
        print(f"   共 {total_modules} 个模块出现问题")
        print(f"   总计 {total_logs} 条 {args.level} 日志")
        
        if args.check_json:
            invalid_count = sum(len(mod.get("invalid_json_lines", [])) for mod in result.values())
            print(f"   JSON 校验失败: {invalid_count} 行")
            
    except FileNotFoundError:
        print(f"❌ 错误: 日志文件未找到 '{args.input}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ 分析失败: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()