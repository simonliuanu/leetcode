# recursion solution:
class Solution:
    @cache # this decorator stores previous calculated results in cache, makes this solution very fast
    def fib(self, n: int) -> int:
        return n if n < 2 else self.fib(n - 1) + self.fib(n - 2)

# dp solution:
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        ans = 0
        for _ in range(2, n + 1):
            ans = a + b
            a, b = b, ans
        return ans
