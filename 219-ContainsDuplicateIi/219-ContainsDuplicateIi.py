# Last updated: 21.02.2026, 21:00:08
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        meeted = {}
        
        for index,num in enumerate(nums):
            
            if num in meeted:
                for i in meeted[num]:
                    if abs(index-i) <= k:
                        return True

                meeted[num].append(index)
            else:
                meeted[num] = [index]
        return False 



        