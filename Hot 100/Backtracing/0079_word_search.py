class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        used = [[False] * col for _ in range(row)]

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if (r < 0 or r >= row
                or c < 0 or c >= col
                or used[r][c]
                or board[r][c] != word[i]):
                return False

            used[r][c] = True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if dfs(r + dr, c + dc, i + 1):
                    return True
            used[r][c] = False

            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False

# A Better Solution:
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])

        def dfs(x: int, y: int, i: int) -> bool:
            if board[x][y] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            board[x][y] = ''
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + dx < r and 0 <= y + dy < c and dfs(x + dx, y + dy, i + 1):
                    return True
            board[x][y] = word[i]

        return any(dfs(x, y, 0) for x in range(r) for y in range(c))
