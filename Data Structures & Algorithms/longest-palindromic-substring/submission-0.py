class Solution:
    def find_palin(self, left, right, s):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        left += 1
        right -= 1
        return (left , right - left + 1)
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 0
        for i in range(len(s)):
            s1, l1 = self.find_palin(i, i, s)
            if l1 > max_len:
                max_len = l1
                start = s1
            s2, l2 = self.find_palin(i, i+1, s)
            if l2 > max_len:
                max_len = l2
                start = s2
        return s[start: start + max_len]