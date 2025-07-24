class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i, j in enumerate(nums):
            if i <= rightmost:
                rightmost = max(rightmost, i + j)
                if rightmost >= n - 1:
                    return True
        return False
