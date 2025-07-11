# shell sort using default gap sequence:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        gap = n >> 1

        while gap >= 1:
            for i in range(gap, n):
                tmp = nums[i]
                j = i - gap
                while j >= 0 and nums[j] > tmp:
                    nums[j + gap] = nums[j]
                    j -= gap
                nums[j + gap] = tmp
            gap >>= 1

        return nums


# shell sort using Knuth gap sequence:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # construct a Knuth sequence
        gaps = []
        k = 1
        while (3**k - 1)//2 < n:
            gaps.append((3**k - 1)//2)
            k += 1
        for gap in reversed(gaps):
            for i in range(gap, n):
                tmp = nums[i]
                j = i - gap
                while j >= 0 and nums[j] > tmp:
                    nums[j + gap] = nums[j]
                    j -= gap
                nums[j + gap] = tmp
        return nums


