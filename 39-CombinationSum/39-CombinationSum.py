# Last updated: 5.01.2026, 14:09:40
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        solution = set()
4        
5
6        def recu(number,tab):
7            if number == target:
8                solution.add(tuple(sorted(tab[:])))
9                return
10            elif number> target:
11                return 
12            else:
13                for candidate in candidates:
14                    tab.append(candidate)
15                    recu(number+candidate,tab)
16                    tab.pop()
17            
18        recu(0,[])
19        res = [list(x) for x in solution]
20        
21        return res