# 回文串问题
"""
Leetcode.3.125 的 Docstring
1.先将字符串处理去除所有非所有非字母数字字符，判断是否处理完为空串
2.然后将处理完的字符串进行大写转小写
3.将处理后得到的纯字母数字字符串进行首尾的交换得到字符串2
4.将字符串1和字符串2进行匹配，如果完全相同，那么返回true，否则返回false
5.采用双指针法 -- 不会创建实例字符串不占内存，不会爆内存，适合 大内存/大文件/流失处理
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # 模拟左侧非字母数字元素
            while left < right and not s[left].isalnum():
                left += 1
                
            # 模拟过滤右侧非字母数字元素
            while left <right and not s[right].isalnum():
                right -= 1
                
            # 模拟转小写比较
            if s[left].lower() != s[right].lower():
                return False
            
            # 继续往中间走
            left += 1
            right -= 1
            
        return True