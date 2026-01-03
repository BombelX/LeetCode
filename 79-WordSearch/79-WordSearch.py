# Last updated: 3.01.2026, 20:47:15
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        n = len(board)
4        m = len(board[0])
5
6        moves = [(-1,0),(1,0),(0,-1),(0,1)]
7        def dfs(x,y,candidate,visited):
8            if candidate == word:
9                return True
10            if len(candidate) >= len(word):
11                return False
12            for dx,dy in moves:
13                new_x,new_y = x+dx,y+dy
14
15                if (new_x,new_y) in visited:
16                    continue
17                if 0 <= new_x < n and 0 <= new_y < m:
18                    if board[new_x][new_y] == word[len(candidate)]:
19                        visited.add((new_x,new_y))
20                        
21                        
22                        res = dfs(new_x,new_y,candidate+board[new_x][new_y],visited)
23                        if res:
24                            return True
25                        visited.remove((new_x,new_y))
26            return False
27
28
29        for i in range(n):
30            for j in range(m):
31                if board[i][j] == word[0]:
32                    r = dfs(i, j, board[i][j], {(i, j)})
33                    if r :
34                        return True
35        return False
36        