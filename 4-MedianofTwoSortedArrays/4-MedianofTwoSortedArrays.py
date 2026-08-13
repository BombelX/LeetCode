# Last updated: 13.08.2026, 23:58:00
        n, m = len(nums1), len(nums2)
        total_left = (n + m + 1) // 2
        
        left, right = 0, n
        
        while left <= right:
            partitionX = (left + right) // 2
            partitionY = total_left - partitionX
            
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == n else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == m else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # ✅ Znaleźliśmy poprawny podział
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1