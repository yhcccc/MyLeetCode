----------------------------------------------------------------
### 127  
My backtrack solution(DFS): Time limit exceeded(19/39  test cases passed)
```py
class Solution:
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        if endWord not in wordList: return 0
        resPath = []
        self.backtrack(endWord, wordList, resPath, [beginWord])
        if not resPath: return 0
        lengthList = [len(a) for a in resPath]
        lengthList.sort()
        return lengthList[0]
        
    def backtrack(self, endWord, wordList, resPath, wordPath):
        word_cur = wordPath[-1]
        if self.wordCmp(word_cur, endWord):
            resPath.append(wordPath+[endWord])
            return
        for i, word in enumerate(wordList):
            if self.wordCmp(word_cur, word):
                self.backtrack(endWord, wordList[:i]+wordList[i+1:], resPath, wordPath+[word])
        
    def wordCmp(self, A, B):
        cmpList = zip(list(A), list(B))
        dissim = len([a for a, b in cmpList if a != b])
        return True if dissim == 1 else False
```

**BFS(Obviously faster)**  
TC&SC: O(M*N)  
```py
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                combo_dict[word[:i] + '*' + word[i+1:]].append(word)
                
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        
        while queue:
            cur_word, level = queue.pop(0)
            for i in range(L):
                intermediate_word = cur_word[:i] + '*' + cur_word[i+1:]
                
                for word in combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                combo_dict[intermediate_word] = []
        return 0
```

Better algorithm: Bidirectional breadth first search
```py
from collections import defaultdict
class Solution:
    def __init__(self):
        self.length = 0
        self.combo_dict = defaultdict(list)
        
    def visitWordNode(self, queue, visited, other_visited):
        cur_word, level = queue.pop(0)
        for i in range(self.length):
            intermediate_word = cur_word[:i] + '*' + cur_word[i+1:]

            for word in combo_dict[intermediate_word]:
                if word in other_visited:
                    return level + other_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        self.length = len(beginWord)
        
        for word in wordList:
            for i in range(self.length):
                self.combo_dict[word[:i] + '*' + word[i+1:]].append(word)
                
        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]
        visited_bigin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None
        
        while queue_begin and queue_end:
            
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans: return ans
            
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans: return ans
        return 0
```
-------------------

### 126    
##BFS(Dijkstra)##    
``py
from collections import defaultdict
class Solution:
    def __init__(self):
        self.results = []
        self.path = defaultdict(list)

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        queue = [beginWord]
        ladder = {}
        maxL = len(wordList) + 1
        for word in wordList:
            ladder[word] = maxL
        ladder[beginWord] = 0
        # print(ladder)
        # Initialization for minL
        minL = maxL
        
        # BFS: dijsktra algorithm
        while queue:
            # print(queue)
            word = queue.pop(0)
            step = ladder[word] + 1
            # print(step)
            if step > minL: break 
            for i in range(0, len(word)):
                for ch in string.ascii_lowercase:
                    neigh = word[:i] + ch + word[i+1:]
                    # print(neigh)
                    if neigh in ladder:
                        if step > ladder[neigh]: continue
                        elif step < ladder[neigh]:
                            queue.append(neigh)
                            ladder[neigh] = step
                            # print(queue)
                            # print(ladder)
                            
                        # Build adjacent gragh
                        self.path[neigh].append(word)
                        # print(self.path)
                        
                        if neigh == endWord:
                            minL = step
        
        # Backtrack
        self.backtrack(endWord, beginWord, [])
        return self.results
    
    def backtrack(self, word, beginWord, result):
        if word == beginWord:
            self.results.append([beginWord] + result)
            return
        if word in self.path:
            for neigh in self.path[word]:
                self.backtrack(neigh, beginWord, [word] + result)              
``

The DFS could be simplied to 
``py
res = [[endWord]]
while res and res[0][0] != beginWord:
    res = [[p]+r for r in res for p in path[r[0]]]
return res        
``

##Bidirectional BFS##  
``py
from collections import defaultdict
class Solution:
    # Bidirectional-BFS
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if endWord not in wordList: return []
        
        def add_path(tree, word, neigh, is_forw):
            if is_forw: tree[word].append(neigh)
            else: tree[neigh].append(word)
        
        # is_forw: make sure we construct the tree in the correct direction
        def bfs_level(lev_a, lev_b, tree, is_forw, wordSet):
            if not lev_a: return False
            if len(lev_a) > len(lev_b):
                return bfs_level(lev_b, lev_a, tree, not is_forw, wordSet)
            # remove words on current both ends from the dict
            wordSet -= (wordSet & (lev_a | lev_b))
            # as we only need the shortest paths
            # we use a boolean value help early termination
            lev_next, done = set(), False
            while lev_a:
                word = lev_a.pop()
                for c in string.ascii_lowercase:
                    for i in range(len(word)):
                        neigh = word[:i] + c + word[i+1:]
                        if neigh in lev_b:
                            done = True
                            add_path(tree, word, neigh, is_forw)
                        # Make sure we construct the shortest tree 
                        if not done and neigh in wordSet:
                            lev_next.add(neigh)
                            add_path(tree, word, neigh, is_forw)
            return done or bfs_level(lev_next, lev_b, tree, is_forw, wordSet)
        
        def construct_paths(source, dest, tree):
            if source == dest:
                return [[source]]
            return [[source] + path for succ in tree[source]
                                    for path in construct_paths(succ, dest, tree)]
        
        tree = defaultdict(list)
        is_found = bfs_level({beginWord}, {endWord}, tree, True, set(wordList))
        return construct_paths(beginWord, endWord, tree) if is_found else []
``
