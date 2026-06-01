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
        if not head:
            return
        dummy = Node(0)
        dummy.next = head
        curr = head
        
        # interleave copies in the list
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        
        curr = head
        
        # assign random ptr
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        copied_list = head.next
        curr = head

        # return just copy nodes
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = curr.next.next if curr.next else None
            curr = curr.next


        return copied_list


        

