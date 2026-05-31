# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(prev, curr):
            if not curr:
                # we are at the end of the list
                return prev
            last = helper(curr, curr.next)
            curr.next = prev
            return last
        
        return helper(None, head)
        

