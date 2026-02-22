// Last updated: 22.02.2026, 22:33:35
1class Solution {
2public:
3
4    vector<vector<int>> merge(vector<vector<int>>& intervals) {
5        sort(intervals.begin(), intervals.end());
6        vector<vector<int>> new_intervals;
7        new_intervals.push_back(intervals[0]);
8        int new_interval = 0;
9        for (int i = 1; i < intervals.size(); ++i) {
10            if (new_intervals.back()[1] >= intervals[i][0]) {
11                new_intervals.back()[1] = max(new_intervals.back()[1], intervals[i][1]);
12            }
13            else{
14                new_intervals.push_back(intervals[i]);
15            }
16        }
17        return new_intervals;
18    }
19};