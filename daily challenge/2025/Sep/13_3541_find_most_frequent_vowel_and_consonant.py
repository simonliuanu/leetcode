# self solution
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = defaultdict(int)
        consonant = defaultdict(int)
        for c in s:
            if c in 'aeiou':
                vowel[c] += 1
            else:
                consonant[c] += 1
        return max(vowel.values(), default=0) + max(consonant.values(), default=0)
