# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        def helper(root):
            nonlocal max_path
            if not root:
                return float('-inf')
            left_max = helper(root.left)
            right_max = helper(root.right)

            # max if we joined the two max paths at the root
            joined = left_max + root.val + right_max
            # max if we add the root to one of the paths
            max_root = max(left_max + root.val, right_max + root.val, root.val)
            max_path = max(joined, max_root, max_path)
            return max_root
        helper(root)
        return max_path
    