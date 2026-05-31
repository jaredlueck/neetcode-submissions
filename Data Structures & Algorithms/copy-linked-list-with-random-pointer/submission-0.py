"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        def get_node(node):
            nonlocal node_map
            if not node:
                return
            if node in node_map:
                return node_map[node]
            else:
                new_node = Node(node.val)
                node_map[node] = new_node
                return new_node
        
        node = head
        prev = dummy = Node(0)
        while node:
            new_node = get_node(node)
            new_random_node = get_node(node.random)
            new_node.random = new_random_node
            prev.next = new_node
            prev = new_node
            node = node.next
        return dummy.next