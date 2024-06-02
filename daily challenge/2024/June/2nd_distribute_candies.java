class Solution {
    public int distributeCandies(int[] candyType) {
        Set<Integer> set = new HashSet<>();
        int cnt = 0;
        for (int i = 0; i < candyType.length; i++) {
            if (!set.contains(candyType[i])) {
                set.add(candyType[i]);
                cnt++;
            }
            if (cnt == candyType.length / 2) return cnt;
        }
        return cnt;
    }
}
