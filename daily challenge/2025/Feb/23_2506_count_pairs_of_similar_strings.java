class Solution {
    public int similarPairs(String[] words) {
        int cnt = 0;
        for (int i = 0; i < words.length; i++) {
            for (int j = i + 1; j < words.length; j++) {
                if (areSimilar(words[i], words[j])) {
                    cnt++;
                }
            }
        }
        return cnt;
    }

    public boolean areSimilar(String s1, String s2) {
        HashSet<Character> set1 = new HashSet<>();
        HashSet<Character> set2 = new HashSet<>();

        for (char c : s1.toCharArray()) {
            set1.add(c);
        }

        for (char c : s2.toCharArray()) {
            set2.add(c);
        }

        return set1.equals(set2);
    }
}

