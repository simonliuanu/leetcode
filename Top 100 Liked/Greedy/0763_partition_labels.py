#self solution:
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = [0] * 26
        for i, c in enumerate(s):
            d[ord(c) - ord('a')] = i
        ans = []
        l = 0
        r = d[ord(s[0]) - ord('a')]
        for i, c in enumerate(s):
            if i == r:
                ans.append(r - l + 1)
                l = r + 1
                if l < len(s):
                    r = d[ord(s[l]) - ord('a')]
            else:
                r = max(r, d[ord(c) - ord('a')])
        return ans

# slightly optimised:
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = [0] * 26
        for i, c in enumerate(s):
            d[ord(c) - ord('a')] = i
        ans = []
        l = r = 0
        for i, c in enumerate(s):
            r = max(r, d[ord(c) - ord('a')])
            if i == r:
                ans.append(r - l + 1)
                l = r + 1
        return ans

# dict solution:
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {c: i for i, c in enumerate(s)}
        ans = []
        l = r = 0
        for i, c in enumerate(s):
            r = max(r, d[c])
            if i == r:
                ans.append(r - l + 1)
                l = r + 1
        return ans
