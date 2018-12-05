-------------------------
**1.Personal idea**  
When len(l) - l.count('.') != len(set(l)) - 1 happens, it means invalid.
```py
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            l = board[i]
            if len(l) - l.count('.') != len(set(l)) - 1:
                return False
        for i in range(9):
            l = [x[i] for x in board]
            if len(l) - l.count('.') != len(set(l)) - 1:
                return False
        for i in range(3):
            for j in range(3):
                l = board[3*i][3*j:3*j+3] + board[3*i+1][3*j:3*j+3] + board[3*i+2][3*j:3*j+3]
                if len(l) - l.count('.') != len(set(l)) - 1:
                    return False
        return True
```
And it's the optimized method below.
```py
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            l = board[i]
            if not self.is_unit_valid(l):
                return False
        for i in range(9):
            l = [x[i] for x in board]
            if not self.is_unit_valid(l):
                return False
        for i in range(3):
            for j in range(3):
                l = [board[x][y] for x in range(3*i, 3*i+3) for y in range(3*j, 3*j+3)]
                if not self.is_unit_valid(l):
                    return False
        return True
        
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
```
----------------------------
**2.O(n^2)**  
k = i // 3 * 3 + j // 3 can cleverly give # square.  
```py
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        lrow = [[[0] for i in range(9)] for j in range(9)]
        lcol = [[[0] for i in range(9)] for j in range(9)]
        lbox = [[[0] for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    k = i // 3 * 3 + j // 3
                    if lrow[i][num-1] == 1 or lcol[j][num-1] == 1 or lbox[k][num-1] == 1:
                        return False
                    lrow[i][num-1] = lcol[j][num-1] = lbox[k][num-1] = 1
        return True
```
