# Last updated: 28.05.2025, 20:37:12
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1,n):
            for j in range(i+1):
                x = float('inf')
                if j-1>=0:
                    x = triangle[i-1][j-1]
                if j<i:
                    x = min(x,triangle[i-1][j])
                triangle[i][j] += x
        return min(triangle[-1])