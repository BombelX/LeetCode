# Last updated: 11.06.2025, 14:50:02
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        queue = [(i,i+2) for i in range(0,len(nums)-2)]
        start = 0
        end = len(nums)-2
        cnt = 0
        while start<end:
            x = queue[start]
            start +=1
            if x[1]>(len(nums)-1):
                continue
            delta = nums[x[0]+1]-nums[x[0]]
            fl = False
            for i in range(x[1]-x[0]):
                if nums[x[0]+i+1]-nums[x[0]+i] != delta:
                    fl =True
                    break

            if not fl:
                cnt += 1
                if x[1]+1 <= len(nums):
                    queue.append((x[0],x[1]+1))
                    end+=1
        return cnt