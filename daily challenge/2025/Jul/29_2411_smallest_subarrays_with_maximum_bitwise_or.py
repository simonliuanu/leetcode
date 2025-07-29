# solution 1, logically correct, timeout:
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_or = 0
        max_arr = [0] * n
        for i in range(n - 1, -1, -1):
            max_or |= nums[i]
            max_arr[i] = max_or
        ans = [0] * n
        for i in range(n):
            ret = 0
            j = i
            target = max_arr[j]
            while True:
                ret |= nums[j]
                j += 1
                if j == n or ret == target:
                    break
            ans[i] = j - i
        return ans
