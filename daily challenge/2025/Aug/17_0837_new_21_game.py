# dp solution, out of time:
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0 for _ in range(k + maxPts)]
        for i in range(k, k + maxPts):
            if i <= n:
                dp[i] = 1
        for i in range(k - 1, -1, -1):
            for j in range(1, maxPts + 1):
                dp[i] += dp[i + j] / maxPts
        return dp[0]

# optimised solution:
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0 for _ in range(k + maxPts)]
        s = 0
        for i in range(k, k + maxPts):
            if i <= n:
                dp[i] = 1
                s += 1
        for i in range(k - 1, -1, -1):
            dp[i] = s / maxPts
            s = s - dp[i + maxPts] + dp[i]
        return dp[0]

