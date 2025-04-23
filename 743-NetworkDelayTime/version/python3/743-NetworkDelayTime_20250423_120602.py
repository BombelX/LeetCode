# Last updated: 23.04.2025, 12:06:02
from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue  

            for nei, w in graph[node]:
                nd = d + w
                if nd < dist[nei]:
                    dist[nei] = nd
                    heapq.heappush(heap, (nd, nei))

        ans = max(dist.values())
        return ans if ans < float('inf') else -1


        