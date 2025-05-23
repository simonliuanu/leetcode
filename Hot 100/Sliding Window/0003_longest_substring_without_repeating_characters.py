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
