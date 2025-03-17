class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lng = len(nums)
        cnt = 0
        ind = 0
        for i in range(len(nums)):
            if nums[i] == val:
                cnt+=1
            else:
                nums[ind] = nums[i]
                ind+=1
        print(nums[0:ind])
        return lng-cnt
        