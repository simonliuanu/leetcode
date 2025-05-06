class Solution {
    public int minimumRefill(int[] plants, int capacityA, int capacityB) {
        int a = 0;
        int ketA = capacityA;
        int b = plants.length - 1;
        int ketB = capacityB;
        int cnt  = 0;
        while (a <= b) {
            if (a == b) {
                if (Math.max(ketA, ketB) < plants[a]) cnt++;
                return cnt;
            }
            if (ketA < plants[a]) {
                cnt++;
                ketA = capacityA;
            }
            ketA -= plants[a];
            a++;
            if (ketB < plants[b]) {
                cnt++;
                ketB = capacityB;
            }
            ketB -= plants[b];
            b--;
        }
        return cnt;
    }
}
