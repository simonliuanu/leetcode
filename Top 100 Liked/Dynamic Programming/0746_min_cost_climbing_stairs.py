# recursion dp:
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def min_cost(i):
            if i < 2:
                return cost[i]
            return cost[i] + min(min_cost(i - 1), min_cost(i - 2))

        n = len(cost)
        return min(min_cost(n - 1), min_cost(n - 2))

# iteration dp:
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            tmp = cost[i] + min(a, b)
            a, b = b, tmp
        return min(a, b)
