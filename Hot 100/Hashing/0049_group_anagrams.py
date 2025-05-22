class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets: defaultdict[str, List[str]] = defaultdict(list);
        for s in strs:
            key = ''.join(sorted(s));
            buckets[key].append(s);
        return list(buckets.values());

