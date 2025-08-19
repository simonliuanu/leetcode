# self solution:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = r = 0
        while r < n:
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        r = l
        while r < n:
            if nums[r] == 1:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

# slightly optimised:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        for r in range(l, len(nums)):
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        for r in range(l, len(nums)):
            if nums[r] == 1:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

# one-pass(Dutch national flag) solution:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = m = 0
        h = len(nums) - 1
        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
