class Solution {
    public String baseNeg2(int n) {
        if (n == 0) return "0";

        String ret = new String();

        while (n != 0) {
            if (n % -2 == 0) ret = "0" + ret;
            else {
                n -= 1;
                ret = "1" + ret;
            }
            n /= -2;
        }
        return ret;
    }
}
