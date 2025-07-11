# merge sort solution:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) >> 1
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            ret = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    ret.append(left[i])
                    i += 1
                else:
                    ret.append(right[j])
                    j += 1
            ret.extend(left[i:])
            ret.extend(right[j:])
            return ret

        return merge_sort(nums)

