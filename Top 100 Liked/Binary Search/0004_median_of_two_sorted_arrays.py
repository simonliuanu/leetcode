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

# best solution O(log min(m, n)):
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        l, r = 0, m
        half = (m + n + 1) // 2

        while l <= r:
            i = (l + r) // 2
            j = half - i

            if i < m and nums1[i] < nums2[j - 1]:
                l = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                r = i - 1
            else:
                if i == 0:
                    lmax = nums2[j - 1]
                elif j == 0:
                    lmax = nums1[i - 1]
                else:
                    lmax = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return lmax

                if i == m:
                    rmin = nums2[j]
                elif j == n:
                    rmin = nums1[i]
                else:
                    rmin = min(nums1[i], nums2[j])

                return (lmax + rmin) / 2
