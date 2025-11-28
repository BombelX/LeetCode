# Last updated: 28.11.2025, 22:25:08
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1  
5        
6        while left <= right:
7            mid = (left + right) // 2
8            if nums[mid] == target:
9                return mid
10            elif nums[mid] < target:
11                left = mid + 1
12            else:
13                right = mid - 1
14                
15        return -1