// Last updated: 21.02.2026, 19:23:45
1using namespace std;
2class Solution {
3public:
4    bool isAnagram(string s, string t) {
5        int tab[26];         
6        for (int i = 0; i < s.size() ; i++){
7            tab[((int) s[i])%26] += 1;
8        }
9        for (int i = 0; i < t.size() ; i++){
10            tab[((int) t[i])%26] -= 1;
11        }
12        for (int elem : tab){
13            if (elem != 0){
14                return false;
15            }
16        }
17        return true;
18    }
19};