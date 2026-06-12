# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(curr_max, root):
            nonlocal cnt
            if not root:
                return
            
            if root.val >= curr_max:
                # this is a good node
                cnt += 1
            
            new_max = max(curr_max, root.val)

            dfs(new_max, root.left)
            dfs(new_max, root.right)
        dfs(-101, root)
        return cnt
            