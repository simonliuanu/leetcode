class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()
        diag2 = set()

        board = [['.'] * n for _ in range(n)]

        ans = []

        def dfs(row: int):
            if row == n:
                ans.append([''.join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                dfs(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        dfs(0)
        return ans


