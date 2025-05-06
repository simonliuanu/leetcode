import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> ooc = new HashSet<>();

        int r = -1;
        int max = 0;

        for (int i = 0; i < s.length(); i++) {
            if (i != 0)
                ooc.remove(s.charAt(i - 1));
            while (r + 1 < s.length() && !ooc.contains(s.charAt(r + 1))) {
                ooc.add(s.charAt(r + 1));
                r++;
            }
            max = Math.max(max, r + 1 - i);
        }
        return max;
    }
}
