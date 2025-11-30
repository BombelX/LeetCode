# Last updated: 30.11.2025, 23:04:58
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        non_zero_place = 0
4        for i,num in enumerate(nums):
5            if num != 0:
6                nums[i] = 0
7                nums[non_zero_place] = num
8                non_zero_place += 1
9
10
11            
12        