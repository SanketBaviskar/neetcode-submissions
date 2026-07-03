"""
temp = [30,38,30,36,35,40,28]
                 i
ans =  [0,  0,  0,  0,  0,  0]
stack = [5]

"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(ans)-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
            