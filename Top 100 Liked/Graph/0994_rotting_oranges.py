class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = []
        fresh = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1
                elif x == 2:
                    q.append((i, j))
        ans = 0
        while q and fresh:
            ans += 1
            tmp = []
            for i, j in q:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        fresh -= 1
                        grid[x][y] = 2
                        tmp.append((x, y))
            q = tmp
        return -1 if fresh > 0 else ans
