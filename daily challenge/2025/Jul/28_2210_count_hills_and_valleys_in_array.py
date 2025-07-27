class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n - 1):
            if nums[i] == nums[i - 1]:
                continue
            l, r = i - 1, i + 1
            while l > 0 and nums[i] == nums[l]:
                l -= 1
            while r < n - 1 and nums[i] == nums[r]:
                r += 1
            if (nums[i] > nums[l] and nums[i] > nums[r]) or (nums[i] < nums[l] and nums[i] < nums[r]):
                ans += 1
        return ans

