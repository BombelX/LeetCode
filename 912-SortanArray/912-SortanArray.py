# Last updated: 25.03.2025, 21:20:15
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(start, end, tab):
            pivot_index = random.randrange(start, end + 1)
            tab[end], tab[pivot_index] = tab[pivot_index], tab[end]
            j = start
            for i in range(start, end):
                if tab[i] <= tab[end]:
                    tab[j], tab[i] = tab[i], tab[j]
                    j += 1
            tab[j], tab[end] = tab[end], tab[j]
            return j

        def quick_sort(tab, start, end):
            if start >= end:
                return
            piv = partition(start, end, tab)
            quick_sort(tab, start, piv - 1)
            quick_sort(tab, piv + 1, end)

        def count_sort(tab, unique_set):
            unique_list = list(unique_set)
            quick_sort(unique_list, 0, len(unique_list) - 1)
            counts = [0] * len(unique_list)
            original = tab[:] 
            for num in original:
                counts[unique_list.index(num)] += 1
            index = 0
            for i, cnt in enumerate(counts):
                for _ in range(cnt):
                    tab[index] = unique_list[i]
                    index += 1
            return tab

        unique_set = set(nums)
        num_unique = len(unique_set)
        if num_unique == 1:
            return nums
        if num_unique < 10:
            return count_sort(nums, unique_set)
        quick_sort(nums, 0, len(nums) - 1)
        return nums

