# tests/test_github_client.py

import pytest
from unittest.mock import Mock
from src.github_client import get_github_user


def test_get_github_user_success(monkeypatch):
    # 1. 创建一个 mock 响应对象
    mock_response = Mock()
    mock_response.json.return_value = {
        "login": "octocat",
        "id": 12345,
        "name": "The Octocat"
    }
    mock_response.raise_for_status.return_value = None  # 不抛异常

    # 2. 创建 mock 的 requests.get，让它返回 mock_response
    mock_get = Mock(return_value=mock_response)

    # 3. 用 monkeypatch 替换 requests.get
    monkeypatch.setattr("requests.get", mock_get)

    # 4. 调用被测函数
    user = get_github_user("octocat")

    # 5. 验证结果 & 行为
    assert user["login"] == "octocat"
    assert user["id"] == 12345
    mock_get.assert_called_once_with("https://api.github.com/users/octocat")