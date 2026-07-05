# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
1, 2, 3, None, None, 4, 5 

"""
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        node_str = []
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr == None:
                node_str.append("None")
                continue
            node_str.append(str(curr.val))
            queue.append(curr.left)
            queue.append(curr.right)
        return ",".join(node_str)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_vals = data.split(",")
        if not node_vals or node_vals[0] == "None":
            return None
        curr_root = TreeNode(int(node_vals[0]))
        idx = 0
        queue = deque([curr_root])
        while queue and idx < len(node_vals):
            curr_node = queue.popleft()
            idx += 1
            if node_vals[idx] != "None":
                left_node = TreeNode(int(node_vals[idx]))
                curr_node.left = left_node
                queue.append(left_node)
            idx += 1
            if node_vals[idx] != "None":
                right_node = TreeNode(int(node_vals[idx]))
                curr_node.right = right_node
                queue.append(right_node)
            
        return curr_root


