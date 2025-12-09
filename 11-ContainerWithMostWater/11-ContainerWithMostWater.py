# Last updated: 9.12.2025, 20:30:14
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        max_water = 0
4        n = len(height)
5        p1,p2 = 0,n-1
6
7        while p1!=p2:
8            max_water = max(max_water,(p2-p1)*min(height[p1],height[p2]))
9            if height[p1]>height[p2]:
10                p2-=1
11            else:
12                p1+=1
13        return max_water