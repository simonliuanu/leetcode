# self solution:
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        ans = 0
        while r < n:
            if nums[r] == 0:
                l = r
                while r < n and nums[r] == 0:
                    r += 1
                ans += ((r - l + 1) * (r - l)) // 2
            r += 1
        return ans

# smarter solution:
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        a = ans = 0
        for i in nums:
            if i:
                a = 0
            else:
                a += 1
                ans += a
        return ans

