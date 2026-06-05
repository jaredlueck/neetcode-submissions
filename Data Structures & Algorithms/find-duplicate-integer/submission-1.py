class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = dummy = ListNode(0)
        dummy.next = ListNode(10001)
        dummy.next.prev = dummy

        for num in nums:
            print(num)
            while l.val < num:
                l = l.next
            while l.val > num:
                print(l.val)
                l = l.prev
            if l.val == num:
                return num
            new_node = ListNode(num)
            new_node.prev = l
            new_node.next = l.next
            l.next = new_node
            new_node.next.prev = new_node
            l = new_node

        return -1