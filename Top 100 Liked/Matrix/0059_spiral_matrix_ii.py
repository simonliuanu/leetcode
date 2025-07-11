class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        t = l = 0
        b = r = n - 1
        cnt = 1
        while t < n:
            for i in range(l, r + 1):
                ans[t][i] = cnt
                cnt += 1
            t += 1
            for i in range(t, b + 1):
                ans[i][r] = cnt
                cnt += 1
            r -= 1
            for i in reversed(range(l, r + 1)):
                ans[b][i] = cnt
                cnt += 1
            b -= 1
            for i in reversed(range(t, b + 1)):
                ans[i][l] = cnt
                cnt += 1
            l += 1
        return ans
