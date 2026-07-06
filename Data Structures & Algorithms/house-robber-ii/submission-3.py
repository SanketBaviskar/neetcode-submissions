class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def calc(arr):
            prev, pprev = max(arr[0], arr[1]), arr[0]
            for i in range(2, len(arr)):
                profit = max(prev, pprev + arr[i])
                pprev = prev
                prev = profit
            return prev
        arr1 = nums[1:]
        arr2 = nums[:len(nums) - 1]
        return max(calc(arr1), calc(arr2))