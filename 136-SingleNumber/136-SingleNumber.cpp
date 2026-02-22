// Last updated: 22.02.2026, 20:20:25
1class Solution {
2public:
3    int singleNumber(vector<int>& nums) {
4        ios_base::sync_with_stdio(false);
5        if (nums.size() ==1){
6            return nums[0];
7        }
8
9        int nm = nums[0];
10        for (int i=1; i < nums.size(); i++){
11            nm = nm ^ nums[i];
12        }
13        return nm;
14    }
15};