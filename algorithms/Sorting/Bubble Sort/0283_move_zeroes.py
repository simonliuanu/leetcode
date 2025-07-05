# bubble sort solution(timeout):
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] == 0:
                    tmp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = tmp

# double pointers solution:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = 0
        n = len(nums)
        while r < n:
            if nums[r] != 0:
                tmp = nums[r]
                nums[r] = nums[l]
                nums[l] = tmp
                l += 1
            r += 1

