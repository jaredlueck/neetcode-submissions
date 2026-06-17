# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            nonlocal res
            if not root:
                return (float('inf'), float('-inf'))
            
            (lmin, lmax) = dfs(root.left)
            (rmin, rmax) = dfs(root.right)

            # The tree is valid if the right and left subtree are valid 
            # and the current root is greater than all nodes in the left
            # subtree and less than all nodes in the right subtree
            # 
            # It is greater than all nodes on the left if it is greater
            # largest node in the left.
            #
            # It is less than all nodes on the right if it is less than
            # the smallest node on the right
            valid = True
            if lmax >= root.val or rmin <= root.val:
                print(lmax)
                print(rmax)
                print(root.val)
                valid = False
            
            res = res and valid
            
            return (min(root.val, lmin), max(root.val, rmax))
        
        dfs(root)
        return res
        
