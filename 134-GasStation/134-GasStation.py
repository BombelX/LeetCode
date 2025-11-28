# Last updated: 28.11.2025, 19:21:04
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if set(gas) == 1 and set(cost) == 1:
            return 0
        n = len(gas)
        start_station = 0

        while start_station < n:
            flag = False
            tank = 0
            stacion = start_station

            for _ in range(n):
                tank += gas[stacion] - cost[stacion]
                if tank < 0:
                    if stacion >= start_station:
                        start_station = stacion + 1
                        flag = True
                    else:
                        return -1
                    break
                stacion = (stacion + 1) % n

            if flag:
                continue

            if tank >= 0 and stacion == start_station:
                return start_station

            start_station += 1

        return -1
