# recursion solution:
class Solution:
    @cache # this decorator stores previous calculated results in cache, makes this solution very fast
    def fib(self, n: int) -> int:
        return n if n < 2 else self.fib(n - 1) + self.fib(n - 2)
