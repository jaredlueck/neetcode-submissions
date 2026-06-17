class HeapPoint:

    def __init__(self, point: List[int]):
        self.point = point
        self.distance = self.distance(point)
    # comput distance from thsi point to the origin
    def distance(self, point):
        dist = point[0]**2 + point[1]**2
        return dist

    def __repr__(self):
        return f'({self.point[0]},{self.point[1]})'

    def __lt__(self, other):
        return self.distance < other.distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            hp = HeapPoint(point)
            heapq.heappush(heap, hp)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap).point)
        
        return res