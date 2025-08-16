# self solution:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = dict()
        for i in nums:
            mp[i] = mp.get(i, 0) + 1
        return max(mp, key=mp.get)

# Boyer-Moore solution:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for i in nums:
            if cnt == 0:
                ans = i
                cnt = 1
            elif ans == i:
                cnt += 1
            else:
                cnt -= 1
        return ans
