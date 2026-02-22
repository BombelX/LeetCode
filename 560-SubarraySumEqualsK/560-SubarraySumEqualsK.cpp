// Last updated: 22.02.2026, 21:22:30
1#include <unordered_map>
2
3class Solution {
4public:
5    int subarraySum(vector<int>& nums, int k) {
6        if (nums.size() == 1 ){
7            if (nums[0] == k){
8                return 1;
9            }
10            else{
11                return 0;
12            }
13        }
14
15        unordered_map<int,int> visited;
16        visited[0] = 1;
17        visited[nums[0]] += 1;
18        int res = 0;
19
20        if (nums[0] == k){
21            res +=1;
22        }
23
24        for (int i = 1;i < nums.size(); ++i){
25            nums[i] += nums[i-1];
26            int missing  = nums[i]-k;
27            cout << missing;
28            if (visited.count(missing)>0 ){
29                res += visited[missing];
30            }
31            visited[nums[i]] += 1;
32        }
33        return res;
34
35    }
36};