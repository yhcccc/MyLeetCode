-----------------------
#### I  
**1. Combine**  
O(min(m, n))  
My combine method:(40ms)
```py
class Solution:
    def uniquePaths(self, m, n):
        # Combine calculation
        def combine(i, j):
            if i == 0 or j == 0:
                return 1
            k = i - 1
            l = j - 1
            numerator = i
            denominator = j
            while k > i - j:
                numerator *= k
                k -= 1
            while l > 1:
                denominator *= l
                l -= 1
            return numerator // denominator
         
        return combine(m + n - 2, min(m - 1, n - 1))
```
Optimized:(32ms)
```py
class Solution:
    def uniquePaths(self, m, n):
        N = n + m - 2
        k = min(m - 1, n - 1)
        res = 1
        for i in range(1, k + 1):
            res = res * (N - k + i) // i
        return res
```
**2. Dynamic Planning**  
<https://leetcode.com/problems/unique-paths/discuss/22954/0ms-5-lines-DP-Solution-in-C%2B%2B-with-Explanations>  
The most optimized:  
Time:O(m*n); Space:O(min(m,n))
```py
class Solution:
    def uniquePaths(self, m, n):
        if m > n: return self.uniquePaths(n, m)
        cur = [1 for _ in range(m)]
        for j in range(1, n):
            for i in range(1, m):
                cur[i] += cur[i - 1] 
        return cur[m - 1]
```
-----------------------
#### II  
**Dynamic Planning**  
My DP method:
```py
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1: return 0
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        path = [[0] * n for _ in range(m)]
        path[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 0:
                    if i > 0 and j > 0:
                        path[i][j] = path[i - 1][j] + path[i][j - 1]
                    if i == 0 and j > 0:
                        path[i][j] = path[i][j - 1]
                    if j == 0 and i > 0:
                        path[i][j] = path[i - 1][j]
        return path[m - 1][n - 1]
```
Optimized:space: O(n)
```py
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1: return 0
        m = len(obstacleGrid); n = len(obstacleGrid[0])
        path = [0 for _ in range(n)]
        path[0] = 1
        for row in obstacleGrid:
            for j in range(n):
                if row[j] == 1:
                    path[j] = 0
                elif j > 0:
                    path[j] += path[j - 1]
        return path[n - 1]
```
