# regular solution:
class Solution:
    desc = ("Gold Medal", "Silver Medal", "Bronze Medal")
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [""] * len(score)
        arr = sorted(enumerate(score), key = lambda x: -x[1])
        for i, (idx, _) in enumerate(arr):
            ans[idx] = self.desc[i] if i < 3 else str(i + 1)
        return ans

# shell sort solution:
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        arr = [(score[i], i) for i in range(n)]

        gap = n >> 1
        while gap >= 1:
            for i in range(gap, n):
                tmp = arr[i]
                j = i - gap
                while j >= 0 and arr[j][0] < tmp[0]:
                    arr[j + gap] = arr[j]
                    j -= gap
                arr[j + gap] = tmp
            gap >>= 1

        ans = [""] * n
        for i, (_, j) in enumerate(arr):
            if i == 0:
                ans[j] = "Gold Medal"
            elif i == 1:
                ans[j] = "Silver Medal"
            elif i == 2:
                ans[j] = "Bronze Medal"
            else:
                ans[j] = str(i + 1)

        return ans
