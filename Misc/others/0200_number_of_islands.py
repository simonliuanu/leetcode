# self solution:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col, i, j, grid):
            if grid[i][j] == '1':
                grid[i][j] = '0'
            if i + 1 < row and grid[i + 1][j] == '1':
                bfs(row, col, i + 1, j, grid)
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                bfs(row, col, i - 1, j, grid)
            if j + 1 < col and grid[i][j + 1] == '1':
                bfs(row, col, i, j + 1, grid)
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                bfs(row, col, i, j - 1, grid)

        ans = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ans += 1
                    bfs(row, col, i, j, grid)
        return ans
