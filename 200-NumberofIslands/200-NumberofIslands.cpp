// Last updated: 21.02.2026, 21:11:22
1#include <tuple>
2#include <vector>
3class Solution {
4public:
5    vector<tuple<int, int>> moves {make_tuple(-1,0),make_tuple(0,-1),make_tuple(1,0),make_tuple(0,1)};
6    void dfs(vector<vector<char>>& grid ,int x, int y,int n,int m){
7        if (x < 0  || x >= n || y < 0 || y >= m || grid[x][y] != '1'){
8            return;
9        }
10        grid[x][y] = 'v';
11        
12        for (tuple<int,int> move : moves){
13            int dx= x+get<0>(move);
14            int dy = y+get<1>(move);
15            dfs(grid,dx,dy,n,m);
16        }
17    }
18
19    int numIslands(vector<vector<char>>& grid) {
20        ios_base::sync_with_stdio(false);
21        cin.tie(NULL);
22        int m = grid[0].size();
23        int n = grid.size();
24        int island = 0;
25        for (int i = 0; i<n ; i++){
26            for (int j =0; j<m ; j++){
27                if (grid[i][j] == '1'){
28                    island++;
29                    dfs(grid,i,j,n,m);
30                }
31            }
32        }   
33        return island   ;
34    }
35};