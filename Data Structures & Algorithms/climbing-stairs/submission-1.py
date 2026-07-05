"""
n = 2
str1 = 1
str2 = 2
str3 = 3

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        prev, pprev = 2, 1
        total = 0
        for _ in range(3, n+1):
            total = prev + pprev
            pprev = prev
            prev = total
        return total
        