# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                res.append("null")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return " ".join(res)

    # Decodes your encoded data into a tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree_array = data.split(" ")
        index = 0
        print(tree_array)
        def build():
            nonlocal index
            
            if index >= len(tree_array) or tree_array[index] == "null":
                index += 1
                return
            print(index)
            node = TreeNode(tree_array[index])
            index += 1
            node.left = build()
            node.right = build()

            return node

        return build()
            
