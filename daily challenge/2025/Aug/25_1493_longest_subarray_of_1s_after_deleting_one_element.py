# sliding window
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = cnt = ans = 0
        for r, n in enumerate(nums):
            cnt += 1 - n
            while cnt > 1:
                cnt -= 1 - nums[l]
                l += 1
            ans = max(ans, r - l)
        return ans
