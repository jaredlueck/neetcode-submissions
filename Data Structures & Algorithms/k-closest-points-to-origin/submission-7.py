class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            dist = point[0]**2 + point[1]**2
            return dist
        heap = []
        
        for point in points:
            dist = distance(point)
            heapq.heappush(heap, (dist, point))

        res = []

        for i in range(k):
            (dist, point) = heapq.heappop(heap)
            res.append(point)
        
        return res