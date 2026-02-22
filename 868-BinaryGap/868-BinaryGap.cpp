// Last updated: 22.02.2026, 12:51:08
1using namespace std;
2class Solution {
3public:
4    int binaryGap(int n) {
5        ios_base::sync_with_stdio(false);
6        cin.tie(NULL);
7        int last_1 = -1;
8        int max_dist= -1;
9        int i = 0;
10        while (n > 0){
11            int bit = n % 2;
12            if (bit == 1){
13                if (last_1 != -1){
14                    max_dist = max(max_dist,i-last_1);
15                }
16                last_1 = i;
17            }
18            n /= 2;
19            i++;
20        }
21        return max(max_dist,0);
22    }
23};