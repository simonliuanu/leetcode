# classic dp solution:
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]

# slightly optimised:
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            for j in range(1, isqrt(i) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]
