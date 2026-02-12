line = "2026-02-03 ERROR user_login failed"

print("ERROR" in line)

print(line.split())

error_count = {}
  
# Func2: defaultdict
from collections import defaultdict
error_count = defaultdict(int)
error_count["login"] += 1