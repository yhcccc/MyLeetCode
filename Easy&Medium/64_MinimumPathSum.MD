**Dynamic Planning**  
Finish it just like 62&63.  
Space: O(m*n)
```py
class Solution:
    def minPathSum(self, grid):
        m = len(grid); n = len(grid[0])
        cost = [[0] * (n) for _ in range(m)]
        cost[0][0] = grid[0][0]
        for i in range(1, m):
            cost[i][0] = grid[i][0] + cost[i - 1][0]
        for j in range(1, n):
            cost[0][j] = grid[0][j] + cost[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                cost[i][j] = grid[i][j] + min(cost[i - 1][j], cost[i][j - 1])
        return cost[m - 1][n - 1]
```
Space: O(m*2 or n*2)  
```py
class Solution:
    def minPathSum(self, grid):
        m = len(grid); n = len(grid[0])
        pre = [grid[0][0] for _ in range(m)]
        cur = [0 for _ in range(m)]
        for i in range(1, m):
            pre[i] = pre[i - 1] + grid[i][0]
        for j in range(1, n):
            cur[0] = grid[0][j] + pre[0]
            for i in range(1, m):
                cur[i] = min(cur[i - 1], pre[i]) + grid[i][j]
            cur, pre = pre, cur
        return pre[-1]
```
Space: O(n or m)
```py
class Solution:
    def minPathSum(self, grid):
    
        m = len(grid); n = len(grid[0])
        cost = [0 for _ in range(n)]
        cost[0] = grid[0][0]
        for j in range(1, n):
            cost[j] = cost[j - 1] + grid[0][j]
        for i in range(1, m):
            cost[0] += grid[i][0]
            for j in range(1, n):
                cost[j] = min(cost[j - 1], cost[j]) + grid[i][j]
        return cost[-1]
```
