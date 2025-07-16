class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c not in mp:
                stack.append(c)
            elif not stack or mp[c] != stack.pop():
                return False
        return not stack
