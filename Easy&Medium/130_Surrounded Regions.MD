**DFS**
```py
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ''' 
        Key: Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'
        '''
        def find_neigh(i, j, h, w):
            if board[i][j] == 'O':
                board[i][j] = '1'
                if i > 0:
                    find_neigh(i-1, j, h, w)
                if j > 0:
                    find_neigh(i, j-1, h, w)
                if i < h - 1:
                    find_neigh(i+1, j, h, w)
                if j < w - 1:
                    find_neigh(i, j+1, h, w)
        
        if not board or not board[0]: return
        h, w = len(board), len(board[0])
        
        for i in range(h):
            find_neigh(i, 0, h, w)
            if w > 1:
                find_neigh(i, w-1, h, w)
        
        for j in range(w):
            find_neigh(0, j, h, w)
            if w > 1:
                find_neigh(h-1, j, h, w)
        
        for i in range(h): 
            for j in range(w): 
                if board[i][j]=='O':
                    board[i][j]='X' 
                    
        for i in range(h): 
            for j in range(w): 
                if board[i][j]=='1':
                    board[i][j]='O' 
```
