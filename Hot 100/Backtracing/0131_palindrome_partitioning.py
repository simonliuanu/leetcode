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
