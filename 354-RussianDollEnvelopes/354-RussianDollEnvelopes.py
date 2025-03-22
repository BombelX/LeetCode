// Last updated: 22/03/2025, 10:53:11
import random
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        
        def partition(tab, start, end):
            if end - start == 2:
                if tab[start][0] < tab[start+1][0]:
                    return start+1
                elif tab[start][0] == tab[start+1][0]:
                    if tab[start][1] <= tab[start+1][1]:
                        tab[start], tab[start+1] = tab[start+1], tab[start]
                        return start+1
                    else:
                        return start+1
                else:
                    tab[start], tab[start+1] = tab[start+1], tab[start]
                    return start+1
            
            piv = random.randrange(start, end)
            tab[piv], tab[end-1] = tab[end-1], tab[piv]
            pivot_val = tab[end-1]
            j = start
            
            for i in range(start, end-1):
                if tab[i][0] < pivot_val[0]:
                    tab[j], tab[i] = tab[i], tab[j]
                    j += 1
                elif tab[i][0] == pivot_val[0]:
                    if tab[i][1] > pivot_val[1]:
                        tab[j], tab[i] = tab[i], tab[j]
                        j += 1
            tab[j], tab[end-1] = tab[end-1], tab[j]
            return j

        def quicksort(tab, start, end):
            if end - start < 2:
                return
            pivot = partition(tab, start, end)
            quicksort(tab, start, pivot)
            quicksort(tab, pivot+1, end)
        
        quicksort(envelopes, 0, n)
        print(envelopes)
        #po posortowaniu uzywamy algorytmu LIS aby znalezc dlugosc najdluzszego podciagu rosnacego 
        def lower_bound(dp, x):
            left = 0
            right = len(dp)
            while left < right:
                mid = (left + right) // 2
                if dp[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            return left
        widths = [w for h, w in envelopes]
        print(widths)

        def lis(sequence):
            dp = []
            for x in sequence:
                i = lower_bound(dp, x)
                if i == len(dp):
                    dp.append(x)
                else:
                    dp[i] = x
            return dp
        t = lis(widths)
        return len(t)
                    