class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = nums[0]
        b = inf
        for i in nums:
            if i <= a:
                a = i
            elif i <= b:
                b = i
            elif b < i:
                return True
        return False

