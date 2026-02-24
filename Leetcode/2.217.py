# 217存在重复元素
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for c in nums:
            count[c] += 1
        for i, c in enumerate(nums):
            if count[c] >= 2:
                return True
        return False