# tests/conftest.py

import os
import tempfile
import pytest
from src.log_parser import count_errors_in_file

@pytest.fixture
def temp_log_file():
    """创建一个带测试日志的临时文件，测试完自动删除"""
    # 创建临时文件
    fd, path = tempfile.mkstemp(suffix=".log")
    
    # 写入测试内容
    with os.fdopen(fd, 'w') as tmp:
        tmp.write("INFO: User logged in\n")
        tmp.write("ERROR: Database timeout\n")
        tmp.write("WARNING: Low disk space\n")
        tmp.write("ERROR: Auth failed\n")
    
    # 把路径交给测试函数
    yield path
    
    # 测试结束后自动清理
    os.unlink(path)

def test_count_errors_in_file(temp_log_file):
    """测试日志文件中的 ERROR 计数"""
    error_count = count_errors_in_file(temp_log_file)
    assert error_count == 2  # 我们写了 2 行 ERROR