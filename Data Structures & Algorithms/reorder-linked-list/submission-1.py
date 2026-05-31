# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(prev, curr):
            if not curr:
                return prev
            last = reverse(curr, curr.next)
            curr.next = prev
            return last
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # slow is pointing to head of second half
        head2 = reverse(None, slow.next)
        slow.next = None

        head1 = head
        
        while head2 and head1 != head2:
            tmp = head1.next
            tmp2 = head2.next
            head1.next = head2
            head2.next = tmp
            head1 = tmp
            head2 = tmp2



