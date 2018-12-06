Concatenating the two lists, sorting, and grabbing the middle item passes the leetcode online judge, but it is not O((n+m)log(n+m)) and would never be accepted in an interview (it doesn't even use the sorted structure of the list).   
Using a merge (as in mergesort) is better (O(n+m)) but still isn't what we want.


----------------
The binary search method provided by Solution meets the O(log(min(m,n))) time complexity.  
```py
class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
            
        imin = 0; imax = m; half = (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i
            if (j == 0 or i == m or B[j - 1] <= A[i]) and (i == 0 or j == n or A[i - 1] <= B[j]):
                if i == 0: maxofL = B[j - 1]
                elif j == 0: maxofL = A[i - 1]
                else: maxofL = max(A[i - 1], B[j - 1])
                if (m + n) % 2 != 0:
                    return maxofL
                
                if i == m: minofR = B[j]
                elif j == n: minofR = A[i]
                else: minofR = min(A[i], B[j])
                return (maxofL + minofR) / 2
            elif i < m and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1
```
-----------------------
 O(log(n+ m)) solution
 ```py
 class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def Findkth(i, j, k):
            """
            i: Start index of A
            j: Start index of B
            k: Remaining distance to Median
            """
            if i == len(A): return B[j + k]
            elif j == len(B): return A[i + k]
            elif k == 0: return min(A[i], B[j])

            halfA = min(len(A) - i, (k + 1) // 2)
            halfB = min(len(B) - j, (k + 1) // 2)
            a = A[i + halfA - 1]
            b = B[j + halfB - 1]
            if a > b:
                return Findkth(i, j + halfB, k - halfB)
            else:
                return Findkth(i + halfA, j, k - halfA)
            
        totalLen = len(A) + len(B) 
        if totalLen % 2 != 0:
            return Findkth(0, 0, totalLen // 2)
        else:
            maxL = Findkth(0, 0, totalLen // 2 - 1)
            minR = Findkth(0, 0, totalLen // 2)
            return (maxL + minR) / 2
 ```
