class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        prev, pprev = max(nums[0], nums[1]), nums[0]
        for i in range(2, len(nums)):
            profit = max(prev, pprev + nums[i])
            pprev = prev
            prev = profit
        return prev
