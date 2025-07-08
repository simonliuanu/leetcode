class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return None
        n = len(nums)

        def quick_sort(nums: List[int], l: int, r: int) -> None:
            if l >= r: return
            pivot = partition(nums, l, r)
            quick_sort(nums, l, pivot - 1)
            quick_sort(nums, pivot + 1, r)

        def partition(nums: List[int], l: int, r: int) -> int:
            rd = random.randrange(l, r + 1)
            nums[rd], nums[l] = nums[l], nums[rd]
            i = l
            for j in range(l + 1, r + 1):
                if nums[j] < nums[l]:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[i], nums[l] = nums[l], nums[i]
            return i

        quick_sort(nums, 0, n - 1)

        return nums[n >> 1]
