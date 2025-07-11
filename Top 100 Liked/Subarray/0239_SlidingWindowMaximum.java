// First try, out of time:
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] ans = new int[nums.length - k + 1];
        int l = 0, r = k - 1;
        for (int i = 0; i < nums.length - k + 1; i++) {
            int max = Integer.MIN_VALUE;
            for (int j = l; j <= r; j++) {
                max = Math.max(max, nums[j]);
            }
            ans[i] = max;
            l++;
            r++;
        }
        return ans;
    }
}

// Monotonic deque:
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        Deque<Integer> q = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!q.isEmpty() && nums[q.getLast()] < nums[i]) {
                q.removeLast();
            }
            q.addLast(i);

            if (i - q.getFirst() >= k) {
                q.removeFirst();
            }

            if (i >= k - 1) {
                ans[i - k + 1] = nums[q.getFirst()];
            }
        }
        return ans;
    }
}
