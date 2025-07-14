# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # if not root:
        #     return 0
        ans = 0
        dic = defaultdict(int)
        dic[0] = 1

        def dfs(node: TreeNode, presum: int):
            if not node:
                return

            nonlocal ans
            presum += node.val
            ans += dic[presum - targetSum]

            dic[presum] += 1
            dfs(node.left, presum)
            dfs(node.right, presum)
            dic[presum] -= 1

        dfs(root, 0)
        return ans
