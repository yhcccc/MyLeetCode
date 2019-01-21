Sort solution is not satisfactory.
**Two Pointers**  
My code:  
TC: O(N)  SC: O(N) 
```py
class Solution:
    def sortedSquares(self, A):
        res_N = []
        res_P = []
        res =[]
        for num in A:
            if num <= 0:
                res_N = [num**2] + res_N
            else:
                res_P.append(num**2)
        while res_N and res_P:
            if res_P[0] < res_N[0]:
                num_P = res_P.pop(0)
                res.append(num_P)
            else:
                num_N = res_N.pop(0)
                res.append(num_N)
        if res_N: res += res_N
        if res_P: res += res_P
        return res
```
Simplified to:
```py
class Solution:
    def sortedSquares(self, A):
        N = len(A)
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1
        
        res = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                res.append(A[i]**2)
                i -= 1
            else:
                res.append(A[j]**2)
                j += 1
        
        while i >= 0:
            res.append(A[i]**2)
            i -= 1
        while j < N:
            res.append(A[j]**2)
            j += 1
        
        return res
``` 
```py
class Solution:
    def sortedSquares(self, A):
        ans = []
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                ans.append(left**2)
                l += 1
            else:
                ans.append(right**2)
                r -= 1
        return ans[::-1]
```
