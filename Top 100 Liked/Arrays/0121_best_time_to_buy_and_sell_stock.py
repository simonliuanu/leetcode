class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        f = prices[0]
        for i in prices:
            ans = max(ans, i - f)
            f = min(f, i)
        return ans
