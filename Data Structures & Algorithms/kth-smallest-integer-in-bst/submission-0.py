# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # kth smallest should be the kth node visited
        # in an inorder traversal
        i = 0
        def dfs(root):
            nonlocal i, k
            if not root:
                return
            l = dfs(root.left)
            i += 1
            if i == k:
                return root.val
            r = dfs(root.right)
            return l or r
            
        return dfs(root)
        

            
