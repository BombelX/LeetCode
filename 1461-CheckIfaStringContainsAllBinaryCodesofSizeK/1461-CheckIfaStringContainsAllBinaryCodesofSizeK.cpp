// Last updated: 23.02.2026, 12:16:00
1#include <unordered_map>
2
3class Solution {
4public:
5    bool hasAllCodes(string s, int k) {
6        ios_base::sync_with_stdio(false);
7        cin.tie(NULL);
8        unordered_map<int,bool> map;
9        if (s.size() < k) return false;
10        int tmp = 0;
11        for (int i = 0; i < k ; i++){
12            if(s[i] == '1'){
13                tmp += pow(2,k-i-1);
14            }
15        }
16        map[tmp] = true;
17        // cout<<tmp<<endl;
18
19        for (int i=k; i<s.size(); i++){
20            if(s[i-k] == '1'){
21                tmp -= pow(2,k-1);
22            }
23            tmp = tmp * 2;
24            if(s[i] == '1'){
25                tmp += 1;
26            }
27            map[tmp] = true;
28            // cout<<tmp<<endl;
29            };
30        int limit = pow(2,k)-1;
31        for (int i=0; i<=limit;i++){
32            if (map.count(i) == 0){
33                return false;
34            }
35        }
36        return true;
37    }
38};