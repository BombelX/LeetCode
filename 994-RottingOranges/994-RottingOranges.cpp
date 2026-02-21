// Last updated: 22.02.2026, 00:11:17
1#include <array>
2class Solution {
3public:
4
5    int bfs(vector<vector<int>>& grid, queue<array<int, 3>> q, int n, int m){
6        int moves[5] = {0,1,0,-1,0};
7        int days = 0;
8        while (!q.empty()){
9            array<int, 3> elem = q.front();
10            q.pop();
11            int x = elem[0];
12            int y = elem[1];
13            if (x >= 0 && x<n && y >= 0 && y< m && grid[x][y] == 1){
14                grid[x][y] = 2;
15                days = max(elem[2],days);
16                for (int i = 0; i < 4 ; i++){
17
18                    q.push({x+moves[i],y+moves[i+1],elem[2]+1});
19                }
20            }
21            
22        };
23        return days;
24        
25    }
26
27    
28
29    int orangesRotting(vector<vector<int>>& grid) {
30        queue<array<int, 3>> q;
31        for (int i = 0; i < grid.size() ; i++){
32            for (int j = 0; j < grid[0].size() ; j++){
33                if(grid[i][j] == 2){
34                    grid[i][j] = 1;
35                    q.push({i,j,0});
36                } 
37            }
38        }
39        int res = bfs(grid,q,grid.size(),grid[0].size());
40        for (int i = 0; i < grid.size() ; i++){
41            for (int j = 0; j < grid[0].size() ; j++){
42                if(grid[i][j] == 1){
43                    return -1;
44                } 
45            }
46        }
47        return res;
48    }
49};