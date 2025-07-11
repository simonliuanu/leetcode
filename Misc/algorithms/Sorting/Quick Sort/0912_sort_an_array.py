# quick sort solution, timeout:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quicksort(nums: List[int], l: int, r: int) -> None:
            if l >= r:
                return
            pivot = partition_rand(nums, l, r)
            quicksort(nums, l, pivot - 1)
            quicksort(nums, pivot + 1, r)

        def partition_rand(nums: List[int], l: int, r: int) -> int:
            pivot = random.randrange(l, r + 1)
            nums[pivot], nums[l] = nums[l], nums[pivot]
            i = l
            for j in range(l + 1, r + 1):
                if nums[j] < nums[l]:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[i], nums[l] = nums[l], nums[i]
            return i

        n = len(nums)
        l, r = 0, n - 1
        quicksort(nums, l, r)
        return nums

