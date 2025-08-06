# recursion solution:
class Solution:
    @lru_cache(None) # will timeout without this decorator
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return climbStairs(n - 1) + climbStairs(n - 2)

# iteration solution:
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
