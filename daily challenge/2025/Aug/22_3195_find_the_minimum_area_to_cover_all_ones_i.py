# self solution:
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        u = l = inf
        d = r = -inf
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i < u:
                        u = i
                    if j < l:
                        l = j
                    if i > d:
                        d = i
                    if j > r:
                        r = j
        return (d - u + 1) * (r - l + 1)

