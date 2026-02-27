# src/log_parser.py

def count_errors_in_file(filepath: str) -> int:
    """统计日志文件中包含 'ERROR' 的行数"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return sum(1 for line in lines if "ERROR" in line)
    except FileNotFoundError:
        return 0