class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify_max(nums)

        res = -1000

        for i in range(k):
            res = heapq.heappop_max(nums)
        return res