class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # find row
        b, t = 0, m - 1
        row = -1
        while  b <= t:
            mid = (b + t) // 2
            end_val = matrix[mid][n-1]
            if end_val == target:
                return True
            elif end_val < target:
                b = mid + 1
            elif end_val > target:
                if matrix[mid][0] > target:
                    t = mid - 1
                else:
                    # target must be in this row
                    row = mid
                    break
        if row == -1: return False
        # find col
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            val = matrix[row][mid]
            if  val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1
        return False




