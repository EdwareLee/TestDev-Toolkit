# 采用 enumerate(s) 和 defaultdict方式
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1


"""
 count = defaultdict(int)的意思是将count变成聪明字典，假设后面我在便利一个字符串的每一个元素的时候，
 我只需要采用 count[c] += 1即可实现统计遍历得到字符串s里面每一个元素出现的个数，并且后面我采用
for i, c in enumerate(s)的时候也是一样直接得到(索引,元素)去进行匹配
"""
