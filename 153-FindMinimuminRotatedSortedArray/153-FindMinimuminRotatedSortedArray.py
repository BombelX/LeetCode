# Last updated: 22.08.2026, 21:32:07
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        start = 0
4        end = len(nums)-1
5
6
7        while start<end:
8            mid = (start + end) // 2
9            print(mid,nums[mid])
10            if nums[mid] > nums[end] :
11                start = mid+1
12            else:
13                end = mid
14        # print(mid,nums[mid])
15        
16        return nums[start]
17
18
19        