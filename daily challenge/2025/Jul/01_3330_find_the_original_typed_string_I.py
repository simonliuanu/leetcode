class Solution:
    def possibleString(self, word: str) -> int:
        return sum(1 for i in range(1, len(word)) if word[i] == word[i - 1]) + 1
