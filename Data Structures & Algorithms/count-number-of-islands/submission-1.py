class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(coords):
            # print(coords)
            (x, y) = coords
            grid[x][y] = '0'
            for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                new_x = x + d[0]
                new_y = y + d[1]
                if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]):
                    if grid[new_x][new_y] == '1':
                        dfs((new_x, new_y))
        
        m = len(grid)
        n = len(grid[0])

        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs((i, j))
        return cnt
            