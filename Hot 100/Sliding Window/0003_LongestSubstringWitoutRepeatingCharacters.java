class Solution {
    public int lengthOfLongestSubstring(String s) {
        int r = 0;
        int[] set = new int[128];
        int ans = 0;
        for (int l = 0; l < s.length(); l++) {
            while (r < s.length() && set[s.charAt(r)] == 0) {
                set[s.charAt(r)] = 1;
                r++;
            }
            ans = Math.max(ans, r - l);
            set[s.charAt(l)] = 0;
        }
        return ans;
    }
}
