# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summ = 0
        dummy = curr = ListNode(0)
        carry = 0
        while l1 or l2:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            col_sum = val1 + val2 + carry
            digit = col_sum % 10
            carry = col_sum // 10
            new_node = ListNode(digit)
            curr.next = new_node
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry > 0: curr.next = ListNode(carry)
        return dummy.next