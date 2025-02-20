// Own solution
class Solution {
    public int[] evenOddBit(int n) {
        int even = 0, odd = 0;
        while (n > 0) {
            if (n % 2 == 1) {
                even++;
            }
            n /= 2;
            if (n % 2 == 1) {
                odd++;
            }
            n /= 2;
        }

        return new int[] { even, odd };
    }
}

