// First solution, brute force, O(n^2), really slow
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }

        return new int[2];
    }
}


// Solution 2 using hash map, much faster
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (hashmap.containsKey(target - nums[i])) {
                return new int[]{hashmap.get(target - nums[i]), i};
            }
            hashmap.put(nums[i], i);
        }

        return new int[2];
    }
}
