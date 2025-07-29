class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        max_or = 0
        for i in nums:
            max_or |= i
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            curr = 0
            ret = 0
            j = i
            while j < n and ret != max_or:
                ret |= nums[j]
                curr += 1
            ans[i] = curr
        return ans
