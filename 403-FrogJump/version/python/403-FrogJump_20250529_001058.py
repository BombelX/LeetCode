# Last updated: 29.05.2025, 00:10:58
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        if stones[1]-stones[0] >1:
            return False
        dp = {}
        def jump(stones,k,last):
            nonlocal dp
            if not stones:
                return True
            posible_stones = [last+k-1,last+k,last+k+1]
            if len(stones) == 1:
                if stones[0] in posible_stones:
                    return True
                else:
                    return False
            for i,stone in enumerate(stones):
                if stone >posible_stones[2]: break 
                if stone in posible_stones:
                    if (stone,stone-last) not in dp:
                        x = jump(stones[i+1:],stone-last,stone)
                        if x: return True
                        dp[(stone,stone-last)] = False
            return False
        return jump(stones[1:],1,stones[1])