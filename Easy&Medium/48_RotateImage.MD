**Jigsaw method**  
See <https://leetcode.com/problems/rotate-image/solution/>
The key is to divide the square matrix into four square-like rectangular blocks.
```py
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2 + n%2):
            for j in range(n//2):
                temp = [0] * 4
                row = i
                col = j
                for l in range(4):
                    temp[l] = matrix[row][col]
                    row, col = col, n - 1 - row
                row, col = col, n - 1 - row
                for m in range(4):
                    matrix[row][col] = temp[m]
                    row, col = col, n - 1 - row
```
The algorithm as below is from other's answers. ~~Maybe the use of '[::]' means another matrix created for cache so it doesn't meet the command of the problem.~~  "Because I need to modify the given list object referenced by the variable A. If you do A = ..., then you're instead making the variable A reference another list object, leaving the given one unchanged."
```py
class Solution:
    def rotate(self, matrix):
        matrix[::] = [[matrix[row][col] for row in range(len(matrix))[::-1]] for col in range(len(matrix))][::]
```
```py
class Solution:
    def rotate(self, matrix):
        matrix[::] = zip(*matrix[::-1])
```
