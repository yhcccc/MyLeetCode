**Binary Search**  
O(log(mn))
```py
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        m = len(matrix); n = len(matrix[0])
        row_l = -1; row_h = m
        while row_l + 1 != row_h:
            mid_r = row_l + (row_h - row_l) // 2
            if matrix[mid_r][0] > target:
                row_h = mid_r
            else:
                row_l = mid_r
        if matrix[row_l][0] ==target or matrix[row_l][-1] == target:
            return True
        if row_l < 0 or matrix[row_l][0] > target or matrix[row_l][-1] < target:
            return False
        col_l = -1; col_h = n
        while col_l + 1 != col_h:
            mid_c = col_l + (col_h - col_l) // 2
            if matrix[row_l][mid_c] < target:
                col_l = mid_c
            else:
                col_h = mid_c
        if col_h >= n or matrix[row_l][col_h] != target:
            return False
        return True
```
A more simplified one:
```py
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        m = len(matrix); n = len(matrix[0])
        l = -1; r = m * n
        while l + 1 != r:
            mid = l + (r - l) // 2
            if matrix[mid // n][mid % n] > target:
                r = mid
            else: 
                l = mid
        return matrix[l // n][l % n] == target
```
