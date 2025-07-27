# brute-force(bitwise solution):
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0
        ans = 0
        for i in nums:
            max_val |= i
        for i in range(1, 1 << n):
            curr = 0
            for j in range(n):
                if i >> j & 1:
                    curr |= nums[j]
            if curr == max_val:
                ans += 1
        return ans
