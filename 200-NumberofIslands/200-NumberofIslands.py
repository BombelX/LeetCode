# Last updated: 5.01.2026, 17:14:04
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        
4        visited = set()
5        n = len(grid)
6        m = len(grid[0])
7        moves = [(-1,0),(1,0),(0,1),(0,-1)]
8        islands = 0
9        for x in range(n):
10            for y in range(m):
11                if grid[x][y] == "0" or (x,y) in visited:
12                    continue
13                visited.add((x,y)) 
14                queue = [(x,y)]                
15                ind = 0
16                islands += 1
17                while ind<len(queue):
18                    curr_x, curr_y = queue[ind]
19                    ind += 1
20                    visited.add((curr_x,curr_y))
21                    for dx,dy in moves:
22                        new_x,new_y = curr_x+dx,curr_y+dy
23                        if (0 <= new_x < n) and (0 <= new_y < m):
24                            if (new_x, new_y) not in visited and grid[new_x][new_y] == '1':
25                                visited.add((new_x, new_y))
26                                queue.append((new_x, new_y))
27
28        return islands
29