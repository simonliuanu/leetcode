class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(nums[i])
        return ans

# another in-place solution:
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            tmp = abs(nums[i])
            if nums[tmp - 1] > 0:
                nums[tmp - 1] *= -1
            else:
                ans.append(tmp)
        return ans
