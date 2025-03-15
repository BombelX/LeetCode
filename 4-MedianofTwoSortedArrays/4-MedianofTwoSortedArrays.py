class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        t1,t2 = nums1,nums2
        n,m = len(t1),len(t2)
        merged_tab = [0]*(m+n)
        x = 0
        j = 0
        for ind in range(m+n):
            if x<n and j<m:
                if t1[x]<t2[j]:
                    merged_tab[ind] = t1[x] 
                    x+=1
                else:
                    merged_tab[ind] = t2[j]
                    j+=1
            else:
                if x<n:
                    merged_tab[ind] = t1[x]
                    x+=1
                else:
                    merged_tab[ind] = t2[j]
                    j+=1
        # print(merged_tab)
        if (n+m)%2 == 0:
            return (merged_tab[int((n+m)//2)-1] + merged_tab[int((n+m)//2)])/2
        else :
            return merged_tab[int((n+m)/2)]
        
                    

        
        
        
                    

        
        