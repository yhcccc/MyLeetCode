**DFS**  
```py
class Solution:
    def exist(self, board, word):
        if not word or not board: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.findADJ(board, i, j, word, 0):
                        return True
        return False
    
    def findADJ(self, board, i, j, word, k):
        if k == len(word): return True
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
            return False
        if board[i][j] != word[k]: return False
        temp = board[i][j]
        board[i][j] = '*'
        flag = self.findADJ(board, i+1, j, word, k+1) or \
               self.findADJ(board, i-1, j, word, k+1) or \
               self.findADJ(board, i, j+1, word, k+1) or \
               self.findADJ(board, i, j-1, word, k+1)
        board[i][j] = temp
        return flag
```
