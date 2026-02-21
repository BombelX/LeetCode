// Last updated: 21.02.2026, 20:59:51
using namespace std;
#include <vector>



class Solution {
public:
    vector<bool> Esieve(int range) {
        vector<bool> primes(range + 1, true);
        if (range >= 0) primes[0] = false;
        if (range >= 1) primes[1] = false;

        for (int i = 2; i * i <= range; i++) { 
            if (primes[i]) {
                for (int j = i * i; j <= range; j += i) {
                    primes[j] = false;
                }
            }
        }
        return primes;
    }

    int countPrimeSetBits(int left, int right) {
        int max_prime = log2(right)+1;
        vector<bool> primes = Esieve(max_prime);
        // for (int prime : primes){
        //     cout << prime;
        // }


        int res = 0;
        for (int i = left; i<=right; i++){
            int tmp = i;
            int num = 0;
            while (tmp > 0){
                tmp = tmp&(tmp-1);
                num +=1;
            }
            // cout<< num;
            if (primes[num]){
                res++;
            }
        }
        return res;
    }
};