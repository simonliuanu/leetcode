//Backtracing
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(start: int, remain: int, path: List[int]):
            if remain == 0:
                ans.append(list(path))
                return
            if remain < 0:
                return
            for i in range(start, len(candidates)):
                pick = candidates[i]
                if pick > remain:
                    return
                path.append(pick)
                backtrack(i, remain - pick, path)
                path.pop()

        backtrack(0, target, [])

        return ans
