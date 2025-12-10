# Last updated: 10.12.2025, 20:23:28
1class Solution:
2    def findMaxLength(self, nums: List[int]) -> int:
3        first_visitation = {0:-1}
4        max_len = 0
5        count = 0
6        for i,num in enumerate(nums):
7
8            if num == 1:
9                count +=1
10            else:
11                count -=1
12
13            if count in first_visitation:
14                curr_len = i-first_visitation[count]
15                max_len = max(max_len,curr_len)
16            else:
17                first_visitation[count] = i
18        return max_len