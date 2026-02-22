// Last updated: 22.02.2026, 20:14:46
1#include <unordered_map>
2using namespace std;
3class Solution {
4public:
5    vector<int> twoSum(vector<int>& nums, int target) {
6        ios_base::sync_with_stdio(false);
7        
8        unordered_map<int,int> visited;
9        vector<int> tab(2);
10        
11        int n = nums.size();
12        cout << n << endl;
13        for (int i=0 ;i<n; ++i){
14            int missing = target - nums[i];
15            if (visited.count(missing) > 0){
16                tab[0] = visited[missing];
17                tab[1] = i;
18                break;
19            }
20            visited[nums[i]] = i;
21        }
22        return tab;
23    }
24};