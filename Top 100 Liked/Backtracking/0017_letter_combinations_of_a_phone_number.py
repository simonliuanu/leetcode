class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        ans = []

        def backtrack(idx: int, path: List[str]):
            if idx == len(digits):
                ans.append(''.join(path))
                return

            combo = phone[digits[idx]]

            for ch in combo:
                path.append(ch)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])
        return ans
