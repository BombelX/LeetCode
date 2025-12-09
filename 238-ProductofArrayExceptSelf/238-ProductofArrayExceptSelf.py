# Last updated: 9.12.2025, 19:59:45
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefix_product = [nums[0]]
4        suffix_product = [nums[-1]]
5
6        for num in nums[1:]:
7            prefix_product.append(prefix_product[-1]*num)
8        nums = nums[::-1]
9        for num in nums[1:]:
10            suffix_product.append(suffix_product[-1]*num)
11        suffix_product = suffix_product[::-1]
12        n = len(nums)
13        output = [0]*n
14        for i in range(n):
15            res = 1
16            if i-1>=0:
17                res *= prefix_product[i-1]
18            if i+1<n:
19                res *= suffix_product[i+1]
20            output[i] = res
21        return output
22
23