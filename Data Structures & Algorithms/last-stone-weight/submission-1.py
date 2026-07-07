class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = stones[0]

            if x == y:
                heapq.heappop_max(stones)
            else:
                heapq.heapreplace_max(stones, abs(x-y))
        
        return 0 if not stones else stones[0]