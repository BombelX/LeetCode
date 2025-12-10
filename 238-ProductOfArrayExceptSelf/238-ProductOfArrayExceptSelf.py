# Last updated: 10.12.2025, 20:24:04
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [nums[0]]
        suffix_product = [nums[-1]]

        for num in nums[1:]:
            prefix_product.append(prefix_product[-1]*num)
        nums = nums[::-1]
        for num in nums[1:]:
            suffix_product.append(suffix_product[-1]*num)
        suffix_product = suffix_product[::-1]
        n = len(nums)
        output = [0]*n
        for i in range(n):
            res = 1
            if i-1>=0:
                res *= prefix_product[i-1]
            if i+1<n:
                res *= suffix_product[i+1]
            output[i] = res
        return output

