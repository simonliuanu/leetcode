// Solution using ASCII array instead of hashset
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] m = new int[128];
        int ret = 0;
        for (int i = 0, j = 0; j < s.length(); j++) {
            i = Math.max(m[s.charAt(j)], i);
            m[s.charAt(j)] = j + 1;
            ret = Math.max(ret, j - i + 1);
        }
        return ret;
    }
}
