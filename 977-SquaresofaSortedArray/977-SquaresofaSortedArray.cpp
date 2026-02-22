// Last updated: 22.02.2026, 21:37:45
1class Solution {
2public:
3    vector<int> sortedSquares(vector<int>& nums) {
4        ios_base::sync_with_stdio(false); cin.tie(NULL);
5        int p1 = 0;
6        int p2 = nums.size()-1;
7        int n = p2;
8
9        vector<int> tab(nums.size(),0);
10        for (int i=0;i<nums.size();++i){
11            if (abs(nums[p1]) > abs(nums[p2])){
12                tab[n-i] = nums[p1]*nums[p1];
13                p1++;
14            }
15            else{
16                // cout << p2;
17                tab[n-i] = nums[p2] * nums[p2];
18                p2--;
19            }
20        }
21        return tab;
22    }
23};