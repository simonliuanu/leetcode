# self solution, O(n) extra space:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return list(s)[0]

# O(1) space solution:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans
