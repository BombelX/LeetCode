# Last updated: 5.01.2026, 14:14:36
1
2class Solution:
3    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
4        solution = set()
5        
6        def recu(number,tab,ind):
7            if number == target:
8                solution.add(tuple(tab[:]))
9                return
10            elif number> target:
11                return 
12            else:
13                for i in range(ind,len(candidates)):
14                    tab.append(candidates[i])
15                    recu(number+candidates[i],tab,i)
16                    tab.pop()
17            
18        recu(0,[],0)
19        res = [list(x) for x in solution]
20        
21        return res