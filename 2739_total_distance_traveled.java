class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int cnt = 0;
        int distance = 0;
        while (mainTank > 0) {
            mainTank--;
            distance += 10;
            cnt++;
            if (cnt == 5 && additionalTank > 0) {
                additionalTank--;
                mainTank++;
                cnt = 0;
            }
        }
        return distance;
    }
}
