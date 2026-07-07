class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = abs(heapq.heappop(stones))
            y = abs(stones[0])

            if x == y:
                heapq.heappop(stones)
            else:
                heapq.heapreplace(stones, -1 * abs(x-y))
        
        return 0 if not stones else -1 * stones[0]