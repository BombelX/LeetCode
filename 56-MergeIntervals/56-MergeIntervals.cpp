// Last updated: 22.02.2026, 22:34:06
1class Solution {
2public:
3
4    vector<vector<int>> merge(vector<vector<int>>& intervals) {
5        ios_base::sync_with_stdio(false);
6        cin.tie(NULL);
7        sort(intervals.begin(), intervals.end());
8        vector<vector<int>> new_intervals;
9        new_intervals.push_back(intervals[0]);
10        int new_interval = 0;
11        for (int i = 1; i < intervals.size(); ++i) {
12            if (new_intervals.back()[1] >= intervals[i][0]) {
13                new_intervals.back()[1] = max(new_intervals.back()[1], intervals[i][1]);
14            }
15            else{
16                new_intervals.push_back(intervals[i]);
17            }
18        }
19        return new_intervals;
20    }
21};