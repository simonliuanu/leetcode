class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        used = [False] * n

        def dfs():
            if len(path) == n:
                ans.append(path.copy())
                return
            if len(path) > n:
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs()
                    path.pop()
                    used[i] = False

        dfs()
        return ans

