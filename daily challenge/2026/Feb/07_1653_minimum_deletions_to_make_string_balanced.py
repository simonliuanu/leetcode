class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = bCnt = 0
        for c in s:
            if c == 'b':
                bCnt += 1
            else:
                dp = min(dp + 1, bCnt)
        return dp
