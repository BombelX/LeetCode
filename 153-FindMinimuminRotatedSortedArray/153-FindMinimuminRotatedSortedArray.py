# Last updated: 22.08.2026, 22:52:05
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        start,end  = 0, len(nums)
4
5        while start<end:
6            mid = (start+end) // 2
7            if nums[mid] < target:
8                start = mid+1
9            else:
10                end = mid
11        print(start)
12        return start
13    