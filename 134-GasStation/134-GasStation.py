# Last updated: 3.09.2026, 21:09:50
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3
4
5        start = 0
6        fuel_balance = 0
7        for i in range(len(gas)):
8            fuel_balance += gas[i] - cost[i]
9            if fuel_balance<0:
10                start = i+1
11                fuel_balance = 0
12            
13
14        if  (sum(gas)-sum(cost)) < 0:
15            return -1
16        else:
17            return start
18        # dp = set()
19        # def go(place,fuel,start):
20        #     if (place,fuel) in dp:
21        #         return False
22        #     if fuel<0:
23        #         dp.add((place,fuel))
24        #         return False
25        #     if place == start:
26        #         return True
27
28        #     new_fuel = fuel + gas[place] - cost[place]
29        #     if new_fuel<0:
30        #         dp.add((place,fuel))
31        #         return False
32        #     res = go((place+1)%len(gas),new_fuel,start)
33        #     if res:
34        #         return True
35        #     else:
36        #         dp.add((place,fuel))
37        #         return False
38        # for start,fuel in enumerate(gas):
39        #     if go((start+1)%len(gas),fuel-cost[start],start):
40        #         return start
41
42        return -1
43
44