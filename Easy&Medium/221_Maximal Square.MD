**1.DP(Mine)**
```py
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # DP
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [['0' for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = '1'
                res = 1
            
            
        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = '1'
                res = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    l_pre = min(int(dp[i-1][j]), int(dp[i][j-1]))
                    if l_pre > 0:
                        if dp[i-l_pre][j-l_pre] != '0':
                            l = l_pre + 1
                            dp[i][j] = str(l)
                            res = max(l, res)
                        else:
                            dp[i][j] = str(l_pre)
                    else:
                        dp[i][j] = '1'
                        res = max(1, res)
        return res**2                   
```
**2.DP(Standard)**
```py
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # DP
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    # key 
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(dp[i][j], res)
        return res**2
```
**3.Better DP**  
[Solution](https://leetcode.com/problems/maximal-square/solution/)
```py
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # DP
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        res = 0; pre = 0
        dp = [0 for _ in range(n+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j-1], dp[j], pre) + 1
                    res = max(dp[j], res)
                else:
                    dp[j] = 0
                pre = temp
        return res**2
```
