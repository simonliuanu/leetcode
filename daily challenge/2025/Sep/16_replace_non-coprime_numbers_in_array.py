class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for i in nums:
            while stack and gcd(i, stack[-1]) > 1:
                i = lcm(i, stack.pop())
            stack.append(i)
        return stack
