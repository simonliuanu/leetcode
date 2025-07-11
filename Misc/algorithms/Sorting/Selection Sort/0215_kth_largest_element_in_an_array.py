# selection sort(timeout):
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(k):
            idx = i
            for j in range(i + 1, n):
                if nums[idx] < nums[j]: idx = j
            nums[idx], nums[i] = nums[i], nums[idx]
        return nums[k - 1]
