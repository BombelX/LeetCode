# Last updated: 10.12.2025, 21:08:12
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        if len(nums) <k:
4            return 0
5        
6        sum_k = 0
7        for i in range(k):
8            sum_k += nums[i]
9        left,right = 0,k-1
10        max_sum = sum_k
11
12        for i in range(len(nums)-k) :
13            sum_k -= nums[left]
14            left+=1
15            right+=1
16            sum_k +=nums[right]
17            #print(sum_k)
18            max_sum = max(sum_k,max_sum)
19        return max_sum/k
20            