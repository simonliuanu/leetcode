# O(n) in space:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or k % n == 0:
            return nums
        ans = [0] * n
        for i in range(n):
            ans[(i + k) % n] = nums[i]
        nums[:] = ans
