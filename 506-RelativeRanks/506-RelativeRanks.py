# Last updated: 25.03.2025, 22:20:16
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        tab = score
        def Parent(i):
            return (i-1)//2
        def Left(i):
            return 2*i+1
        def Right(i):
            return 2*i+2
        
        
        def max_heapify(heap,n):
            if len(heap) == 0:
                return
            if n == len(heap)-1:
                return
            largest = heap[n][0]
            if Left(n)<len(heap) and heap[Left(n)][0]>largest:
                largest = heap[Left(n)][0]
            if Right(n)<len(heap) and heap[Right(n)][0]>largest:
                heap[Right(n)],heap[n] = heap[n],heap[Right(n)]
                max_heapify(heap,Right(n))
            elif largest == heap[n][0]:
                return
            else:
                heap[Left(n)],heap[n] = heap[n],heap[Left(n)]
                max_heapify(heap,Left(n))
                
        def max_heapify_up(heap,n):
            if n == 0:
                return
            parent = Parent(n)
            if heap[parent][0]<heap[n][0]:
                heap[parent],heap[n] = heap[n],heap[parent]
                max_heapify_up(heap,parent)
            else:
                return
        heap = []
        for i,score in enumerate(tab):
            heap.append((score,i))
            max_heapify_up(heap,i)

        for i in range(len(tab)):
            tmp = heap[0]
            heap[0] = heap[-1]
            heap.pop(-1)
            max_heapify(heap,0)
            if i == 0:
                tab[tmp[1]] = "Gold Medal"
            elif i ==  1:
                tab[tmp[1]] = "Silver Medal"
            elif i == 2:
                tab[tmp[1]] = "Bronze Medal"
            else:
                tab[tmp[1]] = str(i+1)
        return tab