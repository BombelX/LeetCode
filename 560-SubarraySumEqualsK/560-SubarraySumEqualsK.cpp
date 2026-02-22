// Last updated: 22.02.2026, 21:23:21
1#include <unordered_map>
2
3class Solution {
4public:
5    int subarraySum(vector<int>& nums, int k) {
6        ios_base::sync_with_stdio(false);
7        if (nums.size() == 1 ){
8            if (nums[0] == k){
9                return 1;
10            }
11            else{
12                return 0;
13            }
14        }
15
16        unordered_map<int,int> visited;
17        visited[0] = 1;
18        visited[nums[0]] += 1;
19        int res = 0;
20
21        if (nums[0] == k){
22            res +=1;
23        }
24
25        for (int i = 1;i < nums.size(); ++i){
26            nums[i] += nums[i-1];
27            int missing  = nums[i]-k;
28            // cout << missing;
29            if (visited.count(missing)>0 ){
30                res += visited[missing];
31            }
32            visited[nums[i]] += 1;
33        }
34        return res;
35
36    }
37};