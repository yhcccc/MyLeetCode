**Factorial**  
```py
class Solution:
    def getPermutation(self, n, k):
        res = ''
        k -= 1
        # Create a index list
        list_number = list(range(1, n + 1))
        
        # Create a factorial list
        factorial = [1 for _ in range(n + 1)]
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i
        
        # Find each number in turn
        for j in range(1, n + 1):
            index = k // factorial[n - j]
            res += str(list_number[index])
            list_number.pop(index)
            k -= index * factorial[n - j]
            
        return res
```
