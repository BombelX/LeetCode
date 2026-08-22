# Last updated: 22.08.2026, 19:52:12
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3
4        last_right_index = 0
5        k = 1
6
7        for i,num in enumerate(nums[1:]):
8            if num <= nums[last_right_index]:
9                nums[i+1] = "_"
10            else:
11                last_right_index += 1
12                k+=1
13                nums[last_right_index] = num
14
15        return k
16
17        