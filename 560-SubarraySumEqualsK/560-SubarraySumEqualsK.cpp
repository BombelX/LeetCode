// Last updated: 22.02.2026, 21:23:43
1#include <unordered_map>
2
3class Solution {
4public:
5    int subarraySum(vector<int>& nums, int k) {
6        ios_base::sync_with_stdio(false);
7        cin.tie(NULL);
8        if (nums.size() == 1 ){
9            if (nums[0] == k){
10                return 1;
11            }
12            else{
13                return 0;
14            }
15        }
16
17        unordered_map<int,int> visited;
18        visited[0] = 1;
19        visited[nums[0]] += 1;
20        int res = 0;
21
22        if (nums[0] == k){
23            res +=1;
24        }
25
26        for (int i = 1;i < nums.size(); ++i){
27            nums[i] += nums[i-1];
28            int missing  = nums[i]-k;
29            // cout << missing;
30            if (visited.count(missing)>0 ){
31                res += visited[missing];
32            }
33            visited[nums[i]] += 1;
34        }
35        return res;
36
37    }
38};