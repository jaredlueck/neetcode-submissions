# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        m = set()

        while head:
            if head in m:
                return True
            m.add(head)
            head = head.next
        return False