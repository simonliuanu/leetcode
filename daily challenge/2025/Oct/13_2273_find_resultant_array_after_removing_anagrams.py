class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = [words[0]]
        for i in range(1, n):
            if sorted(words[i]) != sorted(ans[-1]):
                ans.append(words[i])
        return ans
