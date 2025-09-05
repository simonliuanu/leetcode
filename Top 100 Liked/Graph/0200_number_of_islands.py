# self solution:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        s = []
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    s.append((i, j))
                    ans += 1
                    while s:
                        a, b = s.pop()
                        for x, y in (a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1):
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                s.append((x, y))
                                grid[x][y] = '0'
        return ans

# slightly clearer:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    s = [(i, j)]
                    while s:
                        x, y = s.pop()
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            grid[x][y] = '0'
                            s += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return ans
