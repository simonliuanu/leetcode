class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(l: int, r: int, path: List[str]):
            if l == 0 and r == 0:
                ans.append(''.join(path))
                return

            if l > 0:
                path.append('(')
                backtrack(l - 1, r, path)
                path.pop()

            if r > l:
                path.append(')')
                backtrack(l, r - 1, path)
                path.pop()

        backtrack(n, n, [])
        return ans


