class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        presum = min_presum = 0

        for i in nums:
            presum += i
            ans = max(ans, presum - min_presum)
            min_presum = min(min_presum, presum)

        return ans
