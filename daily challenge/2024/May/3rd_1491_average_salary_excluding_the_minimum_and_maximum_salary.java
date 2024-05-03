// My own solution
class Solution {
    public double average(int[] salary) {
        int n = salary.length;
        int sum = salary[0];
        int max = salary[0];
        int min = salary[0];
        for (int i = 1; i < n; i++) {
            sum += salary[i];
            if (salary[i] < min) min = salary[i];
            if (salary[i] > max) max = salary[i];
        }
        return (double) (sum - min - max) / (n - 2);
    }
}
