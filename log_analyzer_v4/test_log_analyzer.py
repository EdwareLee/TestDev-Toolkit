# test_log_analyzer.py
from log_analyzer import parse_log_line

def test_parse_normal_error_line():
    """测试标准 ERROR 日志行"""
    line = "2026-02-10 ERROR module:login from 192.168.1.1: auth failed (code: E1001)"
    result = parse_log_line(line)
    
    assert result["level"] == "ERROR"
    assert result["module"] == "login"
    assert result["ip"] == "192.168.1.1"
    assert result["error_code"] == "E1001"

def test_parse_line_without_module():
    """当日志中没有 'module:xxx' 时，应返回 'unknown'"""
    line = "2026-02-10 ERROR auth failed"
    result = parse_log_line(line)
    
    assert result["module"] == "unknown"
    assert result["level"] == "ERROR"
    assert result["ip"] == "unknown"  # 也没有 IP

def test_parse_line_without_ip():
    """当日志中没有 IP 地址时，ip 应为 'unknown'"""
    line = "2026-02-10 WARNING module:payment: timeout"
    result = parse_log_line(line)
    
    assert result["ip"] == "unknown"
    assert result["module"] == "payment"
    assert result["level"] == "WARNING"

from log_analyzer import analyze_log

def test_analyze_nonexistent_file():
    """当文件不存在时，应返回空字典（不崩溃！）"""
    result = analyze_log("this_file_does_not_exist.log")
    assert result == {}

def test_parse_garbage_or_empty_line():
    """测试各种“脏数据”"""
    # 情况1：空行
    assert parse_log_line("")["module"] == "unknown"
    
    # 情况2：全是乱码
    assert parse_log_line("\x00\x01\x02\x03")["module"] == "unknown"
    
    # 情况3：只有日期
    assert parse_log_line("2026-02-10")["level"] == "INFO"  # 默认 INFO

