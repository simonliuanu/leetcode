class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int ret = 0;
        for (int num : nums) {
            set.add(num);
        }
        for (int num : set) {
            if (!set.contains(num - 1)) {
                int curr = 0;
                while (set.contains(num)) {
                    num++;
                    curr++;
                }
                ret = Math.max(ret, curr);
            }
        }
        return ret;
    }
}
