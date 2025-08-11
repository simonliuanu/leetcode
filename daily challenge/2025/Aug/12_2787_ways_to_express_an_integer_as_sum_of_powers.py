class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 1_000_000_007
        pows = []
        i = 1
        while True:
            p = i ** x
            if p > n:
                break
            pows.append(p)
            i += 1

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        for i in pows:
            for j in range(n, i - 1, -1):
                dp[j] = (dp[j] + dp[j - i]) % MOD
        return dp[n]

