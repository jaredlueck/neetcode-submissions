# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_map = {}

        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        n = len(stack)
        curr = head
        last = stack[n // 2]
        
        for i in range(0, n // 2):
            end = stack.pop()
            tmp = curr.next
            curr.next = end
            end.next = tmp
            curr = tmp
        last.next = None
