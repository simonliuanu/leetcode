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
