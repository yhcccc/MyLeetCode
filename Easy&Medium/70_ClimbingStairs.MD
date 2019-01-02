See <https://leetcode.com/problems/climbing-stairs/solution/>  
**1.Recursion with memorization**  
O(n)
```py
class Solution:
    def climbStairs(self, n):
        memo = [0 for _ in range(n + 1)]
        return self.climb_Stairs(0, n, memo)
        
    def climb_Stairs(self, i, n, memo):
        if i > n:
            return 0
        elif i == n:
            return 1
        elif memo[i] > 0:
            return memo[i]
        memo[i] = self.climb_Stairs(i + 1, n, memo) + self.climb_Stairs(i + 2, n, memo)
        return memo[i]
```
**2.Dynamic Programming**  
O(n)
```py
class Solution:
    def climbStairs(self, n):
        if n == 1: return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1; dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]
```
**3.Fibonacci Number**  
O(n)
```py
class Solution:
    def climbStairs(self, n):
        if n == 1: return 1
        first = 1; second = 2
        third = 0
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second
```
Simplified:  
```py
class Solution:
    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
```
**4.Binets Method**  
O(logN)
```py
class Solution:
    def climbStairs(self, n):
        q = [[1, 1], [1, 0]]
        res = self.MatPow(q, n)
        return res[0][0]
    
    def MatPow(self, a, n):
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if (n & 1) == 1:
                ret = self.MatMul(ret, a)
            n >>= 1
            a = self.MatMul(a, a)
        return ret
    
    def MatMul(self, a, b):
        c = [[0, 0], [0, 0]]
        for i in range(0, 2):
            for j in range(0, 2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c
```
**5.Fibonacci Formula**  
O(logN)
```py
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = math.sqrt(5)
        fibn = pow((1 + a) / 2, n + 1) - pow((1 - a) / 2, n + 1)
        return int(fibn / a)
```
