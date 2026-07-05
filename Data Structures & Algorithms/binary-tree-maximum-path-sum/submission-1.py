# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_sum = -10**20
        def solve(node):
            if not node:
                return 0
            left_sum = max(solve(node.left) , 0)
            right_sum = max(solve(node.right), 0)
            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)
            return node.val + max(left_sum, right_sum)
        solve(root)
        return self.max_sum