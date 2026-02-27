# tests/test_utils.py

import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.utils import extract_domain

@pytest.mark.parametrize(
    "email, expected_domain",
    [
        ("alice@gmail.com", "gmail.com"),
        ("bob@yahoo.com", "yahoo.com"),
        ("charlie@qq.com", "qq.com"),
        ("admin@localhost", "localhost"),
        ("user+tag@sub.domain.co.uk", "sub.domain.co.uk"),
    ]
)
def test_extract_domain_valid_emails(email, expected_domain):
    """批量测试各种合法邮箱"""
    assert extract_domain(email) == expected_domain