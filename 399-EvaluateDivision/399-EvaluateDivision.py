# Last updated: 18.08.2026, 22:37:35
1from collections import defaultdict
2
3class Solution:
4    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
5        seg = defaultdict(defaultdict)
6
7        for i,equation in enumerate(equations):
8            seg[equation[0]][equation[1]] = values[i]
9            seg[equation[1]][equation[0]] = 1/values[i]
10            
11        print(seg)
12        print("-----")
13        answers = []
14        
15        
16        
17            
18            
19        def bfs(start_verticele,target):
20            visited = set()
21            queue = deque([(start_verticele, 1)])
22            
23            while queue:
24                v = queue.popleft()
25                if v[0] == target:
26                    return v[1]
27                if v[0] in visited:
28                    continue
29                print(seg[v[0]])
30                for neigh in seg[v[0]].items():
31                    queue.append((neigh[0],neigh[1]*v[1]))
32                visited.add(v[0])
33            
34            
35        
36            
37            
38        
39        for query in queries:
40
41
42            part1,part2 = query[0],query[1]
43            if part1 not in seg or part2 not in seg:
44                answers.append(-1) 
45                continue
46
47            ans = bfs(part1,part2)
48            if ans:
49                answers.append(ans)   
50            else:
51                answers.append(-1)  
52
53        return answers  