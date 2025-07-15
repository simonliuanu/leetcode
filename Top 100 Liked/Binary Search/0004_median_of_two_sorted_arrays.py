# self solution O(m + n):
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        m, n = len(nums1), len(nums2)
        cnt1 = cnt2 = 0
        while cnt1 < m and cnt2 < n:
            if nums1[cnt1] < nums2[cnt2]:
                nums.append(nums1[cnt1])
                cnt1 += 1
            else:
                nums.append(nums2[cnt2])
                cnt2 += 1
        if cnt1 < m:
            nums.extend(nums1[cnt1:])
        if cnt2 < n:
            nums.extend(nums2[cnt2:])
        n = len(nums)
        if n % 2 == 0:
            return (nums[(n // 2) - 1] + nums[n // 2]) / 2
        else:
            return nums[n // 2]

