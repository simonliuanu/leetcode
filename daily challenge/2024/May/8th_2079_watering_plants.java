// Own solution by simulation
class Solution {
    public int wateringPlants(int[] plants, int capacity) {
        int k = capacity;
        int n = 0;
        int cnt = 0;
        while (n < plants.length) {
            if (k >= plants[n]) {
                k -= plants[n];
                n++;
                cnt++;
            } else {
                cnt += 2 * n;
                k = capacity;
            }
        }
        return cnt;
    }
}
