# Last updated: 28.11.2025, 19:21:17
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
        
#         n = len(nums)
#         if n == 1:
#             return True
#         result = False
#         possible = [-1]*n
#         def jump(pos):
#             nonlocal n,result,possible
#             if result:
#                 return False
#             if pos == n-1:
#                 result = True
#                 return True
#             if pos >n-1:
#                 return False
#             if possible[pos] == 0:
#                 return False
#             else:
#                 flag = False
#                 for i in reversed(range(1,nums[pos]+1)):
#                     res = jump(pos+i)
#                     if res:
#                         flag = True
#                         return True
#                 possible[pos] = 0
#                 return False


#         for i in reversed(range(1,nums[0]+1)):
#             x = jump(i)
#             if x: 
#                 return True

#         return result

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:              # nie da się tu dojść
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1: # meta osiągalna
                return True
        return True