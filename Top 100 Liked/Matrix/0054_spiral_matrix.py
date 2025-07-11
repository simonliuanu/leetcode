class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        while True:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            if top == bottom:
                break
            top += 1
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            if right == left:
                break
            right -= 1
            for i in reversed(range(left, right + 1)):
                ans.append(matrix[bottom][i])
            if bottom == top:
                break
            bottom -= 1
            for i in reversed(range(top, bottom + 1)):
                ans.append(matrix[i][left])
            if left == right:
                break
            left += 1
        return ans
