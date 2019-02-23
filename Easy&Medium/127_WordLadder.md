----------------------------------------------------------------
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


------------------------------------------------
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
