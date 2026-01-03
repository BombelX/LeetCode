# Last updated: 3.01.2026, 19:54:26
1from typing import List
2
3class Solution:
4    def solveNQueens(self, n: int) -> List[List[str]]:
5        cols = set()  
6        pos_diag = set()  # (r - c)
7        neg_diag = set()  # (r + c)
8        res = []
9        board = [["."] * n for _ in range(n)]
10
11        def backtrack(row):
12            if row == n:
13                copy = ["".join(r) for r in board]
14                res.append(copy)
15                return
16
17            for col in range(n):
18                pd = row - col
19                nd = row + col
20                if col in cols or pd in pos_diag or nd in neg_diag:
21                    continue
22                cols.add(col)
23                pos_diag.add(pd)
24                neg_diag.add(nd)
25                board[row][col] = "Q"
26                backtrack(row + 1)
27                cols.remove(col)
28                pos_diag.remove(pd)
29                neg_diag.remove(nd)
30                board[row][col] = "."
31
32        backtrack(0)
33        return res
34            
35            