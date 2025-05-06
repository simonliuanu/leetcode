class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        int i = purchaseAmount;
        int j = purchaseAmount;
        while (i % 10 != 0 && j % 10 != 0) {
            i++;
            j--;
        }

        if (i % 10 == j % 10) {
            purchaseAmount = i;
        } else {
            purchaseAmount = i % 10 == 0 ? i : j;
        }

        return 100 - purchaseAmount;
    }
}
