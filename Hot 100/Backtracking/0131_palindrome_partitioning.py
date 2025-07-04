class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def dfs(start: int):
            if start == n:
                ans.append(path.copy())
            for end in range(start, n):
                str = s[start:end + 1]
                if str == str[::-1]:
                    path.append(str)
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return ans

# Constructing a Palindrome Table First:
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        isPal = [[False] * n for _ in range(n)]

        for i in range(n):
            isPal[i][i] = True
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                if s[i] == s[j] and (L == 2 or isPal[i + 1][j - 1]):
                    isPal[i][j] = True

        ans = []
        path = []

        def dfs(start: int):
            if start == n:
                ans.append(path.copy())
                return True
            for end in range(start, n):
                if isPal[start][end]:
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return ans
