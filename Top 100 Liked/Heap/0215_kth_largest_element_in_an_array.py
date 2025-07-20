# quick sort(timeout):
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quicksort(nums, l, r):
            if l < r:
                p = partition(nums, l, r)
                quicksort(nums, l, p - 1)
                quicksort(nums, p + 1, r)

        def partition(nums, l, r):
            p_idx = random.randrange(l, r + 1)
            nums[p_idx], nums[r] = nums[r], nums[p_idx]
            i = l
            for j in range(l, r):
                if nums[j] < nums[r]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        quicksort(nums, 0, len(nums) - 1)
        return nums[-k]

# optimised quicksort(Dutch National Flag) solution:
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quick(nums, k):
            pivot = random.choice(nums)
            large = []
            small = []
            equal = []
            for i in nums:
                if i > pivot:
                    large.append(i)
                elif i < pivot:
                    small.append(i)
                else:
                    equal.append(i)
            if len(large) >= k:
                return quick(large, k)
            elif len(nums) - len(small) < k:
                return quick(small, k - len(large) - len(equal))
            else:
                return pivot

        return quick(nums, k)


