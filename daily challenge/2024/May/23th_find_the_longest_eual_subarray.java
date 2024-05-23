class Solution {
    public int longestEqualSubarray(List<Integer> nums, int k) {
        Map<Integer, List<Integer>> hashmap = new HashMap<>();
        for (int i : nums) {
            hashmap.computeIfAbsent(nums.get(i), x -> new ArrayList<>()).add(i);
        }
        int ret = 0;
        for (List<Integer> list : hashmap.values()) {
            for (int i = 0, j = 0; i < list.size(); i++) {
                while (list.get(i) - list.get(j) - (i - j) > k) {
                    j++;
                }
                ret = Math.max(ret, i - j + 1);
            }
        }
        return ret;
    }
}
