class Solution:
    def is_palin(self, left, right, s):
        count = 0
        while left >=0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.is_palin(i, i, s)
            count += self.is_palin(i, i+1, s)
        return count