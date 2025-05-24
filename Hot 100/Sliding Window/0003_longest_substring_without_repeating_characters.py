class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        ans = 0
        r = 0
        n = len(s)

        for l in range(n):

            while r < n and s[r] not in occ:
                occ.add(s[r])
                r += 1

            ans = max(ans, r - l)
            occ.remove(s[l])

        return ans

# An optimized solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [0] * 127
        ans = 0
        l = 0
        for r, ch in enumerate(s):
            l = max(arr[ord(ch)], l)
            arr[ord(ch)] = r + 1
            ans = max(ans, r - l + 1)
        return ans

