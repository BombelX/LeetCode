// Last updated: 22.02.2026, 20:13:20
1#include <unordered_map>
2using namespace std;
3class Solution {
4public:
5    vector<int> twoSum(vector<int>& nums, int target) {
6        unordered_map<int,int> visited;
7        vector<int> tab(2);
8        
9        int n = nums.size();
10        cout << n << endl;
11        for (int i=0 ;i<n; ++i){
12            int missing = target - nums[i];
13            if (visited.count(missing) > 0){
14                tab[0] = visited[missing];
15                tab[1] = i;
16                break;
17            }
18            visited[nums[i]] = i;
19        }
20        return tab;
21    }
22};