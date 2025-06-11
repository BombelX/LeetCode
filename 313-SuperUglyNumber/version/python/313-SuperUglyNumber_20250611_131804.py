# Last updated: 11.06.2025, 13:18:04
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = {1}
        heap = [1]
        for _ in range(n-1):
            x = heapq.heappop(heap)
            for p in primes:
                y = x * p
                if y not in seen:
                    seen.add(y)
                    heapq.heappush(heap, y)
        return heap[0]