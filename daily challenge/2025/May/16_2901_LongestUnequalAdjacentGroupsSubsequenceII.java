// First try.
class Solution {
    public List<String> getWordsInLongestSubsequence(String[] words, int[] groups) {
        List<String> ret = new ArrayList<>();
        int current = 0;
        ret.add(words[current]);
        for (int i = 1; i < groups.length; i++) {
            if (groups[current] == groups[i]) break;
            if (hammingDistance(words[current], words[i]) == 1) {
                ret.add(words[i]);
                current = i;
            }
        }
        return ret;
    }

    public int hammingDistance(String a, String b) {
        if (a.length() != b.length()) return -1;
        int ret = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) ret++;
        }
        return ret;
    }
}
