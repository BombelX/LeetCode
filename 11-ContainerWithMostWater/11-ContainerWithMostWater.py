class Solution:
    def maxArea(self, height: List[int]) -> int:
        return maxArea(height)


def maxArea(height: list[int]) -> int:
    i, j = 0, len(height) - 1
    area, maxHeight = 0, max(height)
    while i < j:
        currArea = (j - i) * min(height[i], height[j])
        area = max(currArea, area)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
        if maxHeight * (j - i) <= area:
            break
    return area