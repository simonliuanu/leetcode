class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set(i for i in nums if i > 0)
        return sum(s) if s else max(nums)
