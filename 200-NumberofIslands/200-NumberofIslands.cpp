// Last updated: 21.02.2026, 21:07:53
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
20        int m = grid[0].size();
21        int n = grid.size();
22        int island = 0;
23        for (int i = 0; i<n ; i++){
24            for (int j =0; j<m ; j++){
25                if (grid[i][j] == '1'){
26                    island++;
27                    dfs(grid,i,j,n,m);
28                }
29            }
30        }   
31        return island   ;
32    }
33};