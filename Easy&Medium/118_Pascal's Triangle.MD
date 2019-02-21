```py
class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        if numRows == 0: return []
        res = []
        for i in range(numRows):
            temp = [1 for _ in range(i+1)]
            if i > 1:
                for j in range(1, i):
                    temp[j] = res[i-1][j-1] + res[i-1][j]
            res.append(temp)
        return res
```
