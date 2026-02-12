import re
from collections import defaultdict


def analyze_log(file_path):
    """
    分析日志文件，统计各模块的 ERROR 出现次数。
    :param file_path: 日志文件路径
    :return: dict，如 {"user_login": 3}
    """
    error_modules = defaultdict(int)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or "ERROR" not in line:
                    continue
                # 使用正则表达式匹配
                match = re.search(r"module:(\w+)", line)
                if match:
                    mod = match.group(1)
                    error_modules[mod] += 1
        return dict(error_modules)

    except FileNotFoundError:
        print(f"ERROR: 日志文件 {file_path} 不存在!")
        return {}

    except Exception as e:
        print(f"ERROR: 读取日志时发生异常： {e}")
        return {}
