# Last updated: 28.11.2025, 19:22:58
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        n = len(nums)
4        cntr = 0 
5        k = k%n
6        if k == 0 :return
7        for i in range(k):
8            index = i+k
9            last = nums[i]
10            while cntr < n and index%n !=i:
11                cntr += 1
12                tmp = nums[index%n]
13                nums[index%n] = last
14                last = tmp
15                index += k
16            nums[index%n] = last
17            cntr += 1
18
19            if cntr == n:
20                return nums
21            
22             