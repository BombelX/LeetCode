# Last updated: 28.11.2025, 19:20:01
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        n = len(nums)
4        cntr = 0 
5        for i in range(k):
6            index = i+k
7            last = nums[i]
8            while cntr < n and index%n !=i:
9                cntr += 1
10                tmp = nums[index%n]
11                nums[index%n] = last
12                last = tmp
13                index += k
14            nums[index%n] = last
15            cntr += 1
16
17            if cntr == n:
18                return nums
19            
20             