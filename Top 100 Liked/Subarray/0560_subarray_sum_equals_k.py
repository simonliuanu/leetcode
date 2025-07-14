# Two Traversal
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        occ: dict[int, int] = {}
        ans = 0
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = nums[i] + sums[i]
        for i in range(n + 1):
            ans = ans + occ.get(sums[i] - k, 0)
            occ[sums[i]] = occ.get(sums[i], 0) + 1
        return ans

# One Traversal
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        occ: dict[int, int] = {}
        n = len(nums)
        sums = 0
        occ[0] = 1
        for i in range(n):
            sums = sums + nums[i]
            ans = ans + occ.get(sums - k, 0)
            occ[sums] = occ.get(sums , 0) + 1
        return ans

# simpler solution:
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        presum = 0
        dic = defaultdict(int)
        dic[0] = 1

        for i in nums:
            presum += i
            ans += dic[presum - k]
            dic[presum] += 1

        return ans
