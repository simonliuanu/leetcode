class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        min_diff = float('inf')
        for i in range(n - 1):
            current_diff = arr[i + 1] - arr[i]
            if current_diff < min_diff:
                min_diff = current_diff
        ans = []
        for i in range(n - 1):
            if arr[i + 1] - arr[i] == min:
                ans.append([arr[i], arr[i + 1]])
        return ans
