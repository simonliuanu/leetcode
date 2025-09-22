class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        max_freq = max(d.values())
        return sum(freq for freq in d.values() if freq == max_freq)

# another solution:
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums).values()
        m = max(counts)
        return sum(i for i in counts if i == m)
