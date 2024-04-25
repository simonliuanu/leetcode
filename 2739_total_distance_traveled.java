// Solution by simulation
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

// Solution by mathematical analysis
class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        return 10 * (mainTank + Math.min((mainTank - 1) / 4, additionalTank));
    }
}
