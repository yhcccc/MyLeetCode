-------------------------
I.54  
**Simple method by myself**  
<https://leetcode.com/problems/spiral-matrix/discuss/206486/Easy-to-understand-Python3-32ms-beats-100>
```py
class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        m, n = len(matrix)-1, len(matrix[0])-1
        res = []
        row, col = 0, 0
        for _ in range((m+1) * (n+1)):
            res.append(matrix[row][col])
            if col + 1 >= row and n - col > row and row <= m // 2 or m == 0:
                col += 1
            elif n - col <= row and col - n + m > row and col + 1 > (n+1) // 2 or n == 0:
                row += 1
            elif col - n + m <= row and m - col < row:
                col -= 1
            elif m - col >= row and col + 1 < row:
                row -= 1
        return res
```
More answer could be found at <https://leetcode.com/problems/spiral-matrix/solution/>.  

An amazing answer @ <https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby>.
```py
def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
```
**Explanation:**
```
  spiral_order([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

= [1, 2, 3] + spiral_order([[6, 9],
                            [5, 8],
                            [4, 7]])

= [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                     [5, 4]])

= [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                              [5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

= [1, 2, 3, 6, 9, 8, 7, 4, 5]
```
---------------------
II.59 
Two methods based on I.
```py
class Solution:
    def generateMatrix(self, n):
        if n == 0: return []
        seen = [[False] * n for _ in range(n)]
        ans = [[0] * n for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r, c, di = 0, 0, 0
        for i in range(n * n):
            ans[r][c] = i + 1
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
```
Best:
```py
class Solution:
    def generateMatrix(self, n):
        if n == 0: return []
        res = [[0] * n for _ in range(n)]
        row, col = 0, 0
        for i in range(n * n):
            res[row][col] = i + 1
            if col + 1 >= row and n-1 - col > row:
                col += 1
            elif n-1 - col <= row and col > row:
                row += 1
            elif col <= row and n-1 - col < row:
                col -= 1
            else:
                row -= 1
        return res
```
Amazing again @ <https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions>.  
The 1st method in python3:
```py
class Solution:
    def generateMatrix(self, n):
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + [*zip(*A[::-1])]
        return list(map(list, A))
```
