# Last updated: 29.05.2025, 17:42:35
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total < desiredTotal:
            return False

        if maxChoosableInteger >= desiredTotal:
            return True
        if desiredTotal == 0:
            return True
        dp = {}
        mask = (1 << maxChoosableInteger) - 1

        def play(mask, goal, player):
            key = (mask, goal, player)
            if key in dp:
                return dp[key]

            if goal <= 0:
                dp[key] = False
                return False

            for i in range(maxChoosableInteger):
                if mask & (1 << i):
                    new_mask = mask & ~(1 << i)
                    if not play(new_mask, goal - (i + 1), not player):
                        dp[key] = True
                        return True

            dp[key] = False
            return False
        return play(mask, desiredTotal, True)


