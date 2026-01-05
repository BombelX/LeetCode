# Last updated: 5.01.2026, 16:10:56
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left <= right:
6            mid = (left + right) // 2
7            if nums[mid] == target:
8                return mid
9            if nums[left] <= nums[mid]:
10                if nums[left] <= target < nums[mid]:
11                    right = mid - 1  
12                else:
13                    left = mid + 1  
14            else:
15                if nums[mid] < target <= nums[right]:
16                    left = mid + 1  
17                else:
18                    right = mid - 1
19
20        return -1