class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        path = []
        used = [False for _ in range(n)]

        def dfs():
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return ans
