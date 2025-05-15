class Solution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {

        List<String> ret = new ArrayList<>();
        int current = 0;
        ret.add(words[0]);
        for (int i = 1; i < groups.length; i++) {
            if (groups[current] != groups[i]) {
                ret.add(words[i]);
                current = i;
            }
        }

        return ret;
    }
}

