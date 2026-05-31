# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        node = head
        prev_index = -1
        dummy = prev = ListNode()
        dummy.next = head
        while node:
            if i - prev_index > n:
                # relative distance between 2 pointers is too much, must shrink it by 1
                prev_index += 1
                prev = prev.next
            else:
                # keep incrementing end pointer until we get to the end of the list
                node = node.next
                i += 1
        prev.next = prev.next.next
        return dummy.next
        
            
