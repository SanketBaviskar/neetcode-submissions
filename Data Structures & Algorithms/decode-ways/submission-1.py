class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * (len(s) + 1)
        def solve(idx):
            if idx == len(s):
                return 1
            if dp[idx] != -1:
                return dp[idx]
            count = 0
            if int(s[idx]) != 0:
                count += solve(idx + 1)
            if int(s[idx]) != 0 and idx + 1 < len(s):
                num = int(s[idx]) * 10 + int(s[idx+1])
                if 0 <= num <= 26:
                    count += solve(idx + 2)
            dp[idx] = count
            return count
        return solve(0)
