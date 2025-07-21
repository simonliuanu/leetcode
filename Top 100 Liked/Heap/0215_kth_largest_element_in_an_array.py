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

# max-heap solution:
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def build_max_heap(nums, heap_size):
            for i in range(len(nums) // 2 - 1, -1, -1):
                max_heapify(nums, i, heap_size)

        def max_heapify(nums, i, heap_size):
            left = i * 2 + 1
            right = i * 2 + 2
            target = i

            if left < heap_size and nums[target] < nums[left]:
                target = left
            if right < heap_size and nums[target] < nums[right]:
                target = right
            if target != i:
                nums[target], nums[i] = nums[i], nums[target]
                max_heapify(nums, target, heap_size)

        heap_size = len(nums)
        build_max_heap(nums, heap_size)

        for i in range(len(nums) - 1, len(nums) - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heap_size -= 1
            max_heapify(nums, 0, heap_size)

        return nums[0]
