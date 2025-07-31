# self solution:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col, i, j, grid):
            if grid[i][j] == '1':
                grid[i][j] = '0'
            if i + 1 < row and grid[i + 1][j] == '1':
                dfs(row, col, i + 1, j, grid)
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                dfs(row, col, i - 1, j, grid)
            if j + 1 < col and grid[i][j + 1] == '1':
                dfs(row, col, i, j + 1, grid)
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                dfs(row, col, i, j - 1, grid)

        ans = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(row, col, i, j, grid)
        return ans

# an ai-optimised, seemingly smarter solution, but more time-consuming on leetcode:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x, y):
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                if 0 <= x < row and 0 <= y < col and grid[x][y] == '1':
                    grid[x][y] = '0'
                    stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        row = len(grid)
        col = len(grid[0])
        ans = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans
