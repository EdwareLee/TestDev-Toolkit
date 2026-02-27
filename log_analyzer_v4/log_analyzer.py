import re
from collections import defaultdict

def safe_read_file(path):
    """
    安全地读取文件内容，支持容错处理。
    返回：list of str（每行一个字符串），如果失败则返回空列表 []
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"❌ Error: Log file '{path}' not found.")
        return []
    except UnicodeDecodeError:
        print(f"⚠️ Warning: File '{path}' has encoding issues. Trying latin-1...")
        try:
            with open(path, 'r', encoding='latin-1') as f:
                return f.readlines()
        except Exception:
            print(f"💥 Failed to read file '{path}' with any encoding.")
            return []
    except Exception as e:
        print(f"💥 Unexpected error reading '{path}': {e}")
        return []

def parse_log_line(line: str) -> dict:
    """解析一行日志，返回结构化字典"""
    # 默认返回值（安全兜底）
    result = {
        "level": "INFO",
        "module": "unknown",
        "ip": "unknown",
        "error_code": None
    }
    
    # 简单匹配 ERROR/WARNING
    if "ERROR" in line:
        result["level"] = "ERROR"
    elif "WARNING" in line:
        result["level"] = "WARNING"
    
    # 尝试提取 module（如 module:login）
    module_match = re.search(r"module:(\w+)", line)
    if module_match:
        result["module"] = module_match.group(1)
    
    # 尝试提取 IP（如 from 192.168.1.1）
    ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
    if ip_match:
        result["ip"] = ip_match.group(1)
    
    # 尝试提取 error code（如 (code: E1001)）
    code_match = re.search(r"\(code:\s*(\w+)\)", line)
    if code_match:
        result["error_code"] = code_match.group(1)
    
    return result


def analyze_log(file_path: str) -> dict:
    """分析整个日志文件，返回按模块统计的结果"""
    # from .log_analyzer import safe_read_file  # 假设你已实现 safe_read_file
    lines = safe_read_file(file_path)
    
    lines = safe_read_file(file_path)
    stats = defaultdict(lambda: {"count": 0, "ips": set(), "errors": set()})
    
    for line in lines:
        parsed = parse_log_line(line)
        module = parsed["module"]
        stats[module]["count"] += 1
        if parsed["ip"] != "unknown":
            stats[module]["ips"].add(parsed["ip"])
        if parsed["error_code"]:
            stats[module]["errors"].add(parsed["error_code"])
    
    # 把 set 转成 list，方便测试比较
    for mod in stats:
        stats[mod]["ips"] = list(stats[mod]["ips"])
        stats[mod]["errors"] = list(stats[mod]["errors"])
    
    return dict(stats)