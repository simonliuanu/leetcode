# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion solution:
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans

# iteration solution:
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            node = q.popleft()
            ans.append(node.val)
            if node.right:
                q.appendleft(node.right)
            if node.left:
                q.appendleft(node.left)
        return ans

# Just realized I didn't have to use deque for this operation,
# Even if I want to use deque, pop() and append() to the right will do.
# So here's the simpler
# stack solution:
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        s = [root]
        while s:
            node = s.pop()
            ans.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return ans
