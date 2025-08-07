class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        ans = []
        for i in range(n):
            if i < 2:
                ans.append([1] * (i + 1))
            else:
                tmp = [1] + [0] * (i - 1) + [1]
                for j in range(1, i):
                    tmp[j] = ans[i - 1][j - 1] + ans[i - 1][j]
                ans.append(tmp)
        return ans

# optimised:
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans
