// Simulation
class Solution{
    public int[] distributeCandies(int candies, int num_people) {
        int[] ret = new int[num_people];
        int index = 0;
        int cnt = 1;
        while (candies > 0) {
            if (index == num_people) index = 0;
            if (candies >= cnt) {
                candies -= cnt;
            ret[index] += cnt;}
            else {
            ret[index] += candies;
            candies = 0;
            }
            cnt++;
            index++;
        }
        return ret;
    }
}
