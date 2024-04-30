// Official solution
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int n = s.length();
        if (n < 3) return n;

        int left = 0;
        int right = 0;

        HashMap<Character, Integer> hashmap = new HashMap<>();

        int ret = 2;

        while (right < n) {
            hashmap.put(s.charAt(right), right++);

            if (hashmap.size() == 3) {
                int del = Collections.min(hashmap.values());
                hashmap.remove(s.charAt(del));
                left = del + 1;
            }
            ret = Math.max(ret, right - left);
        }
        return ret;
    }
}
