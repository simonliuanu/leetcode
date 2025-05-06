class Solution {
    public long minimumSteps(String s) {
        long ret = 0;
        long cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                ret += cnt;
            } else {
                cnt++;
            }
        }
        return ret;
    }
}
