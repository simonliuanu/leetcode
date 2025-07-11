// First try, out of time
class Solution {
    public int maxArea(int[] height) {
        int ret = 0;
        for (int i = 0; i < height.length - 1; i++) {
            for (int j = i + 1; j < height.length; j++) {
                int curr = Math.min(height[i], height[j]) * (j - i);
                ret = Math.max(ret, curr);
            }
        }
        return ret;
    }
}

// Two-Pointers Solution
class Solution {
    public int maxArea(int[] height) {
        int ret = 0, l = 0, r = height.length - 1;
        while (l < r) {
            int cur = (r - l) * Math.min(height[l], height[r]);
            ret = Math.max(ret, cur);
            if (height[l] < height[r]) l++;
            else r--;
        }
        return ret;
    }
}

// Optimized Solution
class Solution {
    public int maxArea(int[] height) {
        int ret = 0, l = 0, r = height.length - 1;

        while (l < r) {
            int hl = height[l];
            int hr = height[r];
            int width = r - l;

            if (hl < hr) {
                int area = hl * width;
                ret = ret > area ? ret : area;
                l++;
            } else {
                int area = hr * width;
                ret = ret > area ? ret : area;
                r--;
            }
        }
        return ret;
    }
}
