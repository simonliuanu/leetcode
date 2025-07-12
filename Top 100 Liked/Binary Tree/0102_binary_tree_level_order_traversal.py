# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iteration solution:
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            tmp = []
            new_stack = []
            for i in stack:
                tmp.append(i.val)
                if i.left:
                    new_stack.append(i.left)
                if i.right:
                    new_stack.append(i.right)
            stack = new_stack
            ans.append(tmp)
        return ans

# optimised solution(deque instead of stack):
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            n = len(q)
            tmp = []
            for _ in range(n):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(tmp)
        return ans
