# Last updated: 28.05.2025, 19:20:42
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        sil_tab = [1]
        def silnia(x):
            nonlocal sil_tab
            if x<len(sil_tab):
                return sil_tab[x]
            else:
                res = sil_tab[-1]
                for i in range(len(sil_tab),x+1):
                    res*=i
                    sil_tab.append(res)
            return res
        m = m-1
        n = n-1
        x = n+m
        y = n
        return int(silnia(x)/(silnia(y)*silnia(x-y)))

