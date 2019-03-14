### DFS & BFS  
DFS  
```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        res = 0
        h, w = len(grid), len(grid[0])
        
        def dfs(i, j, h, w):
            grid[i][j] = '0'
            if i > 0 and grid[i-1][j] == '1': dfs(i-1, j, h, w)
            if i < h-1 and grid[i+1][j] == '1': dfs(i+1, j, h, w)
            if j > 0 and grid[i][j-1] == '1': dfs(i, j-1, h, w)
            if j < w-1 and grid[i][j+1] == '1': dfs(i, j+1, h, w)
            
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j, h, w)
                    
        return res
```
BFS
```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        res = 0
        h, w = len(grid), len(grid[0])
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    queue = []
                    queue.append((i, j))
                    while queue:
                        r, c = queue.pop(0)
                        if r > 0 and grid[r-1][c] == '1':
                            queue.append((r-1, c))
                            grid[r-1][c] = '0'
                        if r < h-1 and grid[r+1][c] == '1': 
                            queue.append((r+1, c))
                            grid[r+1][c] = '0'
                        if c > 0 and grid[r][c-1] == '1': 
                            queue.append((r, c-1))
                            grid[r][c-1] = '0'
                        if c < w-1 and grid[r][c+1] == '1': 
                            queue.append((r, c+1))
                            grid[r][c+1] = '0'

        return res
```


-------------------------------
### UnionFind Algorithm  
**1.By Size and with path compression**  
```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        h, w = len(grid), len(grid[0])
        
        uf = UnionFind(grid)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    if i > 0 and grid[i-1][j] == '1':
                        uf.union(i * w + j, (i-1) * w + j)
                    if i < h-1 and grid[i+1][j] == '1': 
                        uf.union(i * w + j, (i+1) * w + j)
                    if j > 0 and grid[i][j-1] == '1': 
                        uf.union(i * w + j, i * w + (j-1))
                    if j < w-1 and grid[i][j+1] == '1': 
                        uf.union(i * w + j, i * w + (j+1))
        return uf.count
                    

class UnionFind:
    # By size
    def __init__(self, grid):
        h, w = len(grid), len(grid[0])
        self.parent = [-1 for _ in range(h * w)]
        self.count = sum(grid, []).count('1')
                    
    def find(self, i):
        # index i
        if self.parent[i] < 0:
            return i
        else:
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
        
    def union(self, x, y):
        # print('1', self.parent, self.count)
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.parent[rootx] > self.parent[rooty]: # Rooty is larger set
                self.parent[rooty] += self.parent[rootx]
                self.parent[rootx] = rooty
            elif self.parent[rootx] == self.parent[rooty]:
                self.parent[rootx] *= 2
                self.parent[rooty] = rootx
            else:
                self.parent[rootx] += self.parent[rooty]
                self.parent[rooty] = rootx
            self.count -= 1
        # print('2', self.parent, self.count)
```
**2.By Rank and with path compression**  
```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        h, w = len(grid), len(grid[0])
        
        uf = UnionFind(grid)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    if i > 0 and grid[i-1][j] == '1':
                        uf.union(i * w + j, (i-1) * w + j)
                    if i < h-1 and grid[i+1][j] == '1': 
                        uf.union(i * w + j, (i+1) * w + j)
                    if j > 0 and grid[i][j-1] == '1': 
                        uf.union(i * w + j, i * w + (j-1))
                    if j < w-1 and grid[i][j+1] == '1': 
                        uf.union(i * w + j, i * w + (j+1))
        return uf.count
                    

class UnionFind:
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        h, w = len(grid), len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    self.parent.append(i * w + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)
                    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]: 
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1
```
Simplified code by eliminating using rankList
```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        h, w = len(grid), len(grid[0])
        
        uf = UnionFind(grid)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    if i > 0 and grid[i-1][j] == '1':
                        uf.union(i * w + j, (i-1) * w + j)
                    if i < h-1 and grid[i+1][j] == '1': 
                        uf.union(i * w + j, (i+1) * w + j)
                    if j > 0 and grid[i][j-1] == '1': 
                        uf.union(i * w + j, i * w + (j-1))
                    if j < w-1 and grid[i][j+1] == '1': 
                        uf.union(i * w + j, i * w + (j+1))
        return uf.count
                    

class UnionFind:
    # By rank
    def __init__(self, grid):
        h, w = len(grid), len(grid[0])
        self.parent = [-1 for _ in range(h * w)] # start at 1(0 and index0 are repeat)
        self.count = sum(grid, []).count('1')
                    
    def find(self, i):
        # index i
        if self.parent[i] < 0:
            return i
        else:
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
        
    def union(self, x, y):
        # print('1', self.parent, self.count)
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.parent[rootx] > self.parent[rooty]: # Rooty is deeper set
                self.parent[rootx] = rooty
            else:
                if self.parent[rootx] == self.parent[rooty]:
                    self.parent[rootx] -= 1
                self.parent[rooty] = rootx
            self.count -= 1
        # print('2', self.parent, self.count)
```
