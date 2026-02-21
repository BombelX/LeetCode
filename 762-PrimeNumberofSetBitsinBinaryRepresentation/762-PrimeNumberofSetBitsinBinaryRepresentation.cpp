// Last updated: 21.02.2026, 20:31:51
1using namespace std;
2#include <vector>
3
4
5
6class Solution {
7public:
8    vector<bool> Esieve(int range) {
9        vector<bool> primes(range + 1, true);
10        if (range >= 0) primes[0] = false;
11        if (range >= 1) primes[1] = false;
12
13        for (int i = 2; i * i <= range; i++) { 
14            if (primes[i]) {
15                for (int j = i * i; j <= range; j += i) {
16                    primes[j] = false;
17                }
18            }
19        }
20        return primes;
21    }
22
23    int countPrimeSetBits(int left, int right) {
24        int max_prime = log2(right)+1;
25        vector<bool> primes = Esieve(max_prime);
26        // for (int prime : primes){
27        //     cout << prime;
28        // }
29
30
31        int res = 0;
32        for (int i = left; i<=right; i++){
33            int tmp = i;
34            int num = 0;
35            while (tmp > 0){
36                tmp = tmp&(tmp-1);
37                num +=1;
38            }
39            // cout<< num;
40            if (primes[num]){
41                res++;
42            }
43        }
44        return res;
45    }
46};