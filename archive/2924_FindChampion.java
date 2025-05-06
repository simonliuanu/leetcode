class Solution {
    public int findChampion(int n, int[][] edges) {
        int[] degrees = new int[n];
        for (int[] e : edges) {
            degrees[e[1]]++;
        }

        int champion = -1;
        for (int i = 0; i < n; i++) {
            if (degrees[i] == 0) {
                if (champion == -1) {
                    champion = i;
                }  else {
                    return -1;
                }
            }
        }
        return champion;
    }
}
