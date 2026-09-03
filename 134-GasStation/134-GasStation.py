# Last updated: 3.09.2026, 21:09:42
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3
4
5        start = 0
6        fuel_balance = 0
7        for i in range(len(gas)):
8            fuel_balance += gas[i] - cost[i]
9            print(i,fuel_balance,start)
10            if fuel_balance<0:
11                start = i+1
12                fuel_balance = 0
13            
14
15        if  (sum(gas)-sum(cost)) < 0:
16            return -1
17        else:
18            return start
19        # dp = set()
20        # def go(place,fuel,start):
21        #     if (place,fuel) in dp:
22        #         return False
23        #     if fuel<0:
24        #         dp.add((place,fuel))
25        #         return False
26        #     if place == start:
27        #         return True
28
29        #     new_fuel = fuel + gas[place] - cost[place]
30        #     if new_fuel<0:
31        #         dp.add((place,fuel))
32        #         return False
33        #     res = go((place+1)%len(gas),new_fuel,start)
34        #     if res:
35        #         return True
36        #     else:
37        #         dp.add((place,fuel))
38        #         return False
39        # for start,fuel in enumerate(gas):
40        #     if go((start+1)%len(gas),fuel-cost[start],start):
41        #         return start
42
43        return -1
44
45