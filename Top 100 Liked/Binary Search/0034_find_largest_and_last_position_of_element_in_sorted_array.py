class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        start = search(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = search(nums, target + 1) - 1
        return [start, end]

