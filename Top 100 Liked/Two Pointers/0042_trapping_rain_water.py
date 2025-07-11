class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        ret = 0
        while l < r:
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)
            if height[l] < height[r]:
                ret += l_max - height[l]
                l += 1
            else:
                ret += r_max - height[r]
                r -= 1
        return ret
