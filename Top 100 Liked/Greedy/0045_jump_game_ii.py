class Solution:
    def jump(self, nums: List[int]) -> int:
        rightmost = 0
        curr = 0
        ans = 0
        for i in range(len(nums) - 1):
            rightmost = max(rightmost, i + nums[i])
            if curr == i:
                curr = rightmost
                ans += 1
        return ans

