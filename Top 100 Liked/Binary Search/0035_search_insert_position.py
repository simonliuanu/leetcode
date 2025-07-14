# self solution:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def search(l, r):
            if l > r:
                return l
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return search(mid + 1, r)
            else:
                return search(l, mid - 1)

        return search(0, len(nums) - 1)

# optimised better solution(iteration):
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l
