import re
from typing import Dict, List

def analyze_log(lines: List[str]) -> Dict:
    """
    Day 2 智能日志解析器
    输入：日志行列表（每行是字符串）
    输出：结构化字典，包含 total_errors, modules, ips, error_codes
    """
    modules = {} # 字典：统计模块出现次数
    ip_set = set() # 集合： 自动去重 IP
    code_set = set() # 集合：自动去重 错误码
    
    # 遍历每一行，用正则提取字段
    for line in lines:
        # 1. 提取模块名：匹配 [xxx]
        mod_match = re.search(r'\[(\w+)\]', line)
        if mod_match:
            module_name = mod_match.group(1)
            modules[module_name] = modules.get(module_name, 0) + 1
            
        # 2. 提取ip
        ip_match = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)
        if ip_match:
            ip_set.add(ip_match.group())
            
        # 3. 提取 错误码
        code_match = re.search(r'code:\s*(E\d+)', line)
        if code_match:
            code_set.add(code_match.group())
            
    return {
            "total errors": len(lines),
            "modules": modules,
            "ips": list(ip_set),
            "codes": list(code_set)
        }    
        
            