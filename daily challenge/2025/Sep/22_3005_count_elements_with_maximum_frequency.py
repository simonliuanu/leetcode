class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        max_freq = max(d.values())
        return sum(freq for freq in d.values() if freq == max_freq)
