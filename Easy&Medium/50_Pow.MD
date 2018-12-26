**Efficient Power**  
Time: O(log n)
```py
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return pow(x * x, n / 2)
        else:
            return pow(x * x, n // 2) * x
```
