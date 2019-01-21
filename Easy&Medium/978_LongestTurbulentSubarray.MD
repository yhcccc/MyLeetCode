My Code:
```py
class Solution:
    def maxTurbulenceSize(self, A):
        l = len(A)
        if l == 0: return 0
        if l == 1: return 1
        rl = 0
        rlmax = 0
        Judge = [1 for _ in range(l - 1)]
        for i in range(0, l - 1):
            if A[i] < A[i + 1]: Judge[i] = -1
            if A[i] == A[i + 1]: Judge[i] = 0
        k = Judge[0]
        for j in Judge[1:]:
            if j != k and j != 0 and k != 0:
                rl += 1
                rlmax = max(rl, rlmax)
            else:
                rl = 0
            k = j
        return rlmax + 2
``` 
**Sliding window**
```py
class Solution:
    def maxTurbulenceSize(self, A):
        l = len(A)
        if l == 1: return 1
        res = 0
        anchor = 0
        def cmp(a, b):
            return (a > b) - (a < b) 
        for i in range(1, l):
            c = cmp(A[i - 1], A[i])
            if i == l- 1 or c * cmp(A[i], A[i + 1]) != -1:
                res = max(res, i - anchor + 1)
                anchor = i
        return res
```
Despite accepted result, it is wrong when input == [2,2] or [9,9].    
Correct solution:  
**DP**  
```py
class Solution:
    def maxTurbulenceSize(self, A):
        mx = 1  # at least 1
        asc, desc = 1, 1  # max len of ascending and descending ending at idx i
        
        for i in range(1, len(A)):
            old = asc
            asc = 1 if A[i] <= A[i - 1] else desc + 1
            desc = 1 if A[i] >= A[i - 1] else old + 1
            mx = max(mx, max(asc, desc))
        return mx
```
