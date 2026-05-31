class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def compute_time(size):
            i = 0
            hours = 0
            while i < len(piles):
                hours += math.ceil(piles[i] / size)
                i += 1
            return hours
        max_stack = max(piles)
        # binary search solution space
        l, r = 1, max_stack
        found = 0
        while l <= r:
            m = (l + r) // 2
            hours = compute_time(m)
            print((m, hours))
            if hours > h:
                l = m + 1
            elif hours <= h:
                # found a solution but try to find an even smaller one
                found = m
                r = m - 1
        return found


