// Own solution
class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] codeM = new int[n];

        for (int i = 0; i < n; i++) {
            if (k == 0) codeM[i] = 0;
            else if (k > 0) {
                int s = 0;
                for (int j = 1; j <= k; j++) {
                    s += code[(i + j) % n];
                }
                codeM[i] = s;
            } else {
                int s = 0;
                for (int j = -1; j >= k; j--) {
                    s += code[((i + j) + n) % n];
                }
                codeM[i] = s;
            }
        }

        return codeM;
    }
}

// Sliding window
class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] ret = new int[n];

        if (k == 0) return ret;

        if (k > 0) {
            int start = 1 % n;
            // int r = (1 + k) % n;
            int sum = 0;
            for (int i = 0; i < k; i++) {
                sum += code[(i + start) % n];
            }
            ret[0] = sum;
            for (int i = 1; i < n; i++) {
                sum -= code[i];
                sum += code[(i + k) % n];
                ret[i] = sum;
            }
        }

        if (k < 0) {
            int start = (-1 + n) % n;
            int sum = 0;
            for (int i = 0; i > k; i--) {
                sum += code[((start + i) % n + n) % n];
            }
            ret[0] = sum;
            for (int i = 1; i < n; i++) {
                sum += code[i - 1];
                sum -= code[((i - 1 + k) % n + n) % n];
                ret[i] = sum;
            }
        }

        return ret;
    }
}
// Sliding window
