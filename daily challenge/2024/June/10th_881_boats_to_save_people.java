class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int l = 0, r = people.length - 1;
        int ret = 0;
        while (l < r) {
            if (people[l] + people[r] > limit) {
                r--;
            } else {
                l++;
                r--;
            }
            ret++;
        }
        if (l == r) return (ret + 1);
        else return ret;
    }
}
