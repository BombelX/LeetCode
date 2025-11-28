# Last updated: 28.11.2025, 22:24:49
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1  # Wskazujemy na ostatni element
5        
6        # Używamy <=, żeby obsłużyć przypadek, gdy zostanie 1 element (left == right)
7        while left <= right:
8            mid = (left + right) // 2
9            
10            if nums[mid] == target:
11                return mid
12            
13            elif nums[mid] < target:
14                # Szukana liczba jest po prawej, więc start musi przeskoczyć mid
15                left = mid + 1
16            else:
17                # Szukana liczba jest po lewej, więc koniec musi przeskoczyć mid
18                right = mid - 1
19                
20        return -1