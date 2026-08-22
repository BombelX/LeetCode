# Last updated: 22.08.2026, 22:52:14
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        start,end  = 0, len(nums)
4        while start<end:
5            mid = (start+end) // 2
6            if nums[mid] < target:
7                start = mid+1
8            else:
9                end = mid
10        return start
11    