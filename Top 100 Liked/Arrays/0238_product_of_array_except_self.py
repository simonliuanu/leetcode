class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]
        tmp = 1
        for i in reversed(range(n)):
            ans[i] *= tmp
            tmp *= nums[i]
        return ans
