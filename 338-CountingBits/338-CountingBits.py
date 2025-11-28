# Last updated: 28.11.2025, 19:20:57
class Solution:
    def countBits(self, n: int) -> List[int]:
        tab = []
        for i in range(n+1):
            tab.append(bin(i).count('1'))
        return tab