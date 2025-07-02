class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      ans = []
      path = []

      def dfs(idx: int):
        if idx == len(nums):
          ans.append(path.copy())
          return

        dfs(idx + 1)

        path.append(nums[idx])
        dfs(idx + 1)
        path.pop()

      dfs(0)
      return ans
