# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        while True:
            # if they are in different subtrees than this is the LCA
            if root.val <= q.val and root.val >= p.val:
                return root
            if root.val >= q.val and root.val <= p.val:
                return root
            # They are in the same subtree so must go down further
            if p.val > root.val:
                root = root.right
            else:
                root = root.left

        

            