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

// A even simpler Solution
class Solution {
    public String baseNeg2(int n) {
        if (n == 0 || n == 1) return String.valueOf(n);
        StringBuilder ret = new StringBuilder();
        while (n != 0) {
            int r = n & 1;
            ret.append(r);
            n -= r;
            n /= -2;
        }
        return ret.reverse().toString();
    }
}
