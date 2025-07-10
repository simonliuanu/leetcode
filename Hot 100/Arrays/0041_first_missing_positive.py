# hash solution(O(1) space not satisfied):
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        for i in nums:
            s.add(i)
        for i in range(1, n + 1):
            if i not in s:
                return i
        return n + 1

# binary search solution(O(n) time complexity not satisfied):
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        def binary_search(nums: List[int], i: int) -> int:
            n = len(nums)
            l, r = 0, n - 1
            while l < r:
                m = (l + r) >> 1
                if nums[m] == i:
                    return m
                elif nums[m] < i:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        n = len(nums)
        nums.sort()
        for i in range(1, n + 1):
            res = binary_search(nums, i)
            if res == -1:
                return i
        return n + 1

