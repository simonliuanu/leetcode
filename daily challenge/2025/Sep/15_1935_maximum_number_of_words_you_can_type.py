class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        words = text.split()
        ans = 0
        for w in words:
            if all(c not in broken for c in w):
                ans += 1
        return ans
