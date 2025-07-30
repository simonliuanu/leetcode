# self solution:
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = 0
        for i in nums:
            target = max(target, i)
        ans = 0
        l = 0
        while l < len(nums):
            if nums[l] == target:
                r = l + 1
                while r < len(nums) and nums[r] == target:
                    r += 1
                ans = max(ans, r - l)
                l = r + 1
            l += 1
        return ans

# smarter solution:
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        curr = 0
        ans = 0
        for i in nums:
            if i == max_val:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 0
        return ans

# an even smarter solution:
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = nums[0]
        curr = 0
        ans = 0
        for i in nums:
            if i > max_val:
                max_val = i
                curr = 1
                ans = 1
            elif i == max_val:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 0
        ans = max(ans, curr)
        return ans
