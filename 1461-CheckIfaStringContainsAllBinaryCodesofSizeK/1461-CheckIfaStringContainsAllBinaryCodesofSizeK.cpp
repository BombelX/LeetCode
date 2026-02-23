// Last updated: 23.02.2026, 12:15:06
1#include <unordered_map>
2
3class Solution {
4public:
5    bool hasAllCodes(string s, int k) {
6        unordered_map<int,bool> map;
7        if (s.size() < k) return false;
8        int tmp = 0;
9        for (int i = 0; i < k ; i++){
10            if(s[i] == '1'){
11                tmp += pow(2,k-i-1);
12            }
13        }
14        map[tmp] = true;
15        // cout<<tmp<<endl;
16
17        for (int i=k; i<s.size(); i++){
18            if(s[i-k] == '1'){
19                tmp -= pow(2,k-1);
20            }
21            tmp = tmp * 2;
22            if(s[i] == '1'){
23                tmp += 1;
24            }
25            map[tmp] = true;
26            // cout<<tmp<<endl;
27            };
28        int limit = pow(2,k)-1;
29        for (int i=0; i<=limit;i++){
30            if (map.count(i) == 0){
31                return false;
32            }
33        }
34        return true;
35    }
36};