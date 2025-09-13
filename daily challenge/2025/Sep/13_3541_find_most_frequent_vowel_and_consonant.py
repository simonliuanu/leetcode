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

# optimised solution:
class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = Counter(s)
        chs = set('aeiou')
        mx1 = mx2 = 0
        for ch, v in cnt.items():
            if ch in chs:
                mx1 = max(mx1, v)
            else:
                mx2 = max(mx2, v)
        return mx1 + mx2
