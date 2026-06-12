# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            node = l
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        dummy = ListNode(0)
        curr = dummy
        while heap:
            val = heapq.heappop(heap)
            new_node = ListNode(val)
            curr.next = new_node
            curr = new_node
        
        return dummy.next