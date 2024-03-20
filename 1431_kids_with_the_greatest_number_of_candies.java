class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        ArrayList<Boolean> bl = new ArrayList<Boolean>();

        for (int i = 0; i < candies.length; i++) {
            boolean flag = true;
            for (int j = 0; j < candies.length; j++) {
                if (!(candies[i] + extraCandies >= candies[j])) {
                    flag = false;
                }
            }
            if (flag) bl.add(true);
            else bl.add(false);
        }

        return bl;
    }

}

