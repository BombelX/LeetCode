# Last updated: 21.05.2025, 17:22:45
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n == 1:
            return True
        result = False
        possible = [-1]*n
        def jump(pos,prev):
            nonlocal n,result,possible
            if result:
                return False
            if pos == n-1:
                result == True
                return True
            if pos >n-1:
                return False
            if possible[pos] == 0:
                return False
            else:
                flag = False
                for i in reversed(range(1,nums[pos]+1)):
                    res = jump(pos+i,pos)
                    if res:
                        flag = True
                        return True
                if not flag:
                    possible[pos] = 0
                else:
                    possible[pos] = 1
                return flag

        for i in reversed(range(1,nums[0]+1)):
            x = jump(i,-1)
            if x: 
                return True

        return result