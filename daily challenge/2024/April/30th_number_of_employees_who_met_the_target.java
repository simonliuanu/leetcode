class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int cnt = 0;
        for (int n : hours) {
            if (n >= target) cnt++;
        }
        return cnt;
    }
}
