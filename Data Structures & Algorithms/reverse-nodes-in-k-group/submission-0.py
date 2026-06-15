# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l, r = head, head
        # prev_k indicates the last node of the previous reversed k-group
        prev_k = None
        while r:
            print((l.val, r.val))
            cnt = k - 1
            # move right pointer to the last node of the current k-group
            while r and cnt > 0:
                r = r.next
                cnt -= 1
            if r and cnt == 0:
                # reverse the k-group
                curr = l
                prev = None
                while prev != r:
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next
                
                if prev_k: 
                    prev_k.next = prev
                else:
                    # new head is the last node of the first k-group
                    head = r
                # leftmost node of k-group will point to the first node of the next k-group
                prev_k = l
                if r:
                    # start the next group
                    l, r = curr, curr
            else:
                # not a complete k-group so do not reverse
                if prev_k:
                    prev_k.next = l
                break
        return head
                
            