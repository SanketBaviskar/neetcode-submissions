"""
[1, 2, 2, 2 + 2, 1 + 2, 1 + 3, 1 + 3]

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, pprev = cost[1], cost[0]
        for i in range(2, len(cost)):
            curr = cost[i] + min(prev, pprev)
            pprev = prev
            prev = curr
        return min(pprev, prev)