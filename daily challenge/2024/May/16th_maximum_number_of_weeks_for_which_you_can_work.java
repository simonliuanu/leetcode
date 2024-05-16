// Original solution, which didn't pass the tests
class Solution {
    public long numberOfWeeks(int[] milestones) {
        int max = milestones[0];
        for (int i = 1; i < milestones.length; i++) {
            if (max < milestones[i]) max = milestones[i];
         }

        int sum = 0;
        for (int i: milestones) {
            sum += i;
        }
        sum -= max;
        if (sum < max) {
            return 2 * sum + 1;
        } else {
            return sum + max;
        }
    }
}

// GPT refined solution, changed int to long to handle the big range
class Solution {
    public long numberOfWeeks(int[] milestones) {
        long max = milestones[0];
        long sum = 0;
        for (int i: milestones) {
            sum += i;
            if (max < i) max = i;
        }

        long rest = sum - max;
        if (rest < max) {
            return 2 * rest + 1;
        } else {
            return sum;
        }
    }
}
