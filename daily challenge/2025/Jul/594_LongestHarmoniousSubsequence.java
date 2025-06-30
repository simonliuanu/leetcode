class Solution {
    public int findLHS(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : nums) {
            // Or use:
            // map.merge(i, 1, Integer::sum)...
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        int ans = 0;
        for (int i : map.keySet()) {
            int c1 = map.get(i);
            // Or use:
            // Integer c2 = map.get(i + 1);
            // if (c2 != null)...
            int c2 = map.getOrDefault(i + 1, 0);
            if (c2 != 0) {
                ans = Math.max(ans, c1 + c2);
            }
        }
        return ans;
    }
}
