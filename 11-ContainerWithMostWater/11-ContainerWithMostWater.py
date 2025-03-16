class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        max_size = 0
        p1,p2 = 0,size-1
        while p1 != p2:
            width = p2-p1
            hg = min(height[p1],height[p2])
            max_size = max(max_size,width*hg)
            if height[p1]>height[p2]:
                p2-=1
            else:
                p1+=1
        return max_size

