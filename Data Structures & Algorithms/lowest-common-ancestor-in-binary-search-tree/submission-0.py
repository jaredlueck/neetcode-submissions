# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(root, node):
            
            if not root: return False
            print("ROOT: " + str(root.val))
            print("NODE: " + str(node.val))
            if root.val == node.val: 
                print("FOUND: " + str(node.val))
                return True
            return search(root.left, node) or search(root.right, node)
        
        while True:
            print(root.val)
            if root == q or root == p:
                return root 
            if search(root.left, p) and search(root.left, q):
                # both in left subtree
                root = root.left
            elif search(root.right, p) and search(root.right, q):
                # both in right subtree
                root = root.right
            else:
                print("FOUND")
                # in different subtrees so this is the common ancester
                return root

            