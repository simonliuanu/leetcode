class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        l = 0
        r = 0
        ans = n + 1
        while r < n:
            sum = sum + nums[r]
            while sum >= target:
                sum = sum - nums[l]
                ans = min(ans, r - l + 1)
                l = l + 1
            r += 1
        if ans == n + 1:
            ans = 0
        return ans
