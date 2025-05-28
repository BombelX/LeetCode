# Last updated: 28.05.2025, 19:18:56
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        for lvl in range(n):
            for box in range(m):
                if (lvl-1>=0) and (box-1>=0):
                    grid[lvl][box] +=min(grid[lvl-1][box],grid[lvl][box-1])
                elif box-1>=0:
                    grid[lvl][box] += grid[lvl][box-1]
                elif lvl-1>=0:
                    grid[lvl][box] += grid[lvl-1][box]
                else:
                    pass
        return grid[-1][-1]

