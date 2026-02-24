import re

line = "2026-02-10 14:25:01 ERROR [user_login] from 192.168.1.105: auth failed (code: E1001)"

"""
1.timestamp: 时间辍
2.ip: ip地址
3.code: 错误码
"""

timestamp = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',line)
ip = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',line)
error_code = re.search(r'code:\s*(E\d+)', line)

print("日志时间： ", timestamp.group())
print("错误主机地址：", ip.group())
print("错误代码: ", error_code.group(1))

"""
提取内容：
1.时间辍：2026-02-10 14:25:01
2.IP地址：192.168.1.105
3.错误码：E1001

"""