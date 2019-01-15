**Backtrack**  
```py
class Solution:
    def combine(self, n, k):
        res = []
        self.backtrack(res, [], 1, n, k)
        return res

    def backtrack(self, res, temp, start, n, k):
        if k == 0:
            res.append(temp[:])
            return
        else:
            for i in range(start, n + 1):
                self.backtrack(res, temp[:] + [i], i + 1, n, k - 1)
```
