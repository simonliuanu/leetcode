class Solution:
    MOD = 1_000_000_007
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        ans = 0
        for _ in range(2, n + 1):
            ans = (a + b) % self.MOD
            a, b = b, ans
        return ans

