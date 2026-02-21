# Last updated: 21.02.2026, 21:00:10
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        n = len(grid)
        m = len(grid[0])
        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        islands = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == "0" or (x,y) in visited:
                    continue
                visited.add((x,y)) 
                queue = [(x,y)]                
                ind = 0
                islands += 1
                while ind<len(queue):
                    curr_x, curr_y = queue[ind]
                    ind += 1
                    visited.add((curr_x,curr_y))
                    for dx,dy in moves:
                        new_x,new_y = curr_x+dx,curr_y+dy
                        if (0 <= new_x < n) and (0 <= new_y < m):
                            if (new_x, new_y) not in visited and grid[new_x][new_y] == '1':
                                visited.add((new_x, new_y))
                                queue.append((new_x, new_y))

        return islands
