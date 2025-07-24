class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pre = [0] * (len(nums) + 1)
        m = {}
        l = 0
        ans = 0
        for i in range(len(nums)):
            pre[i + 1] = pre[i] + nums[i]
            l = max(l, m.get(nums[i], 0))
            m[nums[i]] = i + 1
            ans = max(ans, pre[i + 1] - pre[l])
        return ans
