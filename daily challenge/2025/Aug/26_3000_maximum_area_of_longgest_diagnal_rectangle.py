#self solution:
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        cand = ans = 0
        for i in dimensions:
            d = i[0] ** 2 + i[1] ** 2
            a = i[0] * i[1]
            if d > cand:
                cand = d
                ans = a
            elif d == cand:
                ans = max(a, ans)
        return ans

