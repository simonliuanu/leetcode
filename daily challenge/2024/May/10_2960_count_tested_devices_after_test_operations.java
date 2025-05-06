// Own solution, O(n^2)
class Solution{
    public int countTestedDevices(int[] batteryPercentages) {
        int ret = 0;
        int n = batteryPercentages.length;
        for (int i = 0; i < n; i++) {
            if (batteryPercentages[i] > 0) {
                for (int j = i + 1; j < n; j++) {
                    batteryPercentages[j] = Math.max(0, batteryPercentages[j] - 1);
                }
                ret++;
            }
        }
        return ret;
    }
}

// Solution by difference O(n)
class Solution {
    public int countTestedDevices(int[] batteryPercentages) {
        int n = 0;
        for (int i: batteryPercentages) {
            if (i > n) {
                n++;
            }
        }
        return n;
    }
}
