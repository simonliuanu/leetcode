class Solution:
    def sortVowels(self, s: str) -> str:
        t = list(s)
        v = sorted(c for c in s if c in 'AEIOUaeiou')
        j = 0
        for i, x in enumerate(t):
            if x in 'AEIOUaeiou':
                t[i] = v[j]
                j += 1
        return ''.join(t)
