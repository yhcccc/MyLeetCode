**1.DFS(Best Performance)**  
[Easy, Short, Concise and Fast DFS solution](https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution)  
```py
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def remove(s, last_i, last_j, par):
            stack = 0
            for i in range(last_i, len(s)):
                if s[i] == par[0]: stack += 1
                if s[i] == par[1]: stack -= 1
                if stack >= 0: continue
                for j in range(last_j, i+1):
                    if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                        remove(s[:j] + s[j+1:], i, j, par)
                return 
            
            if par[0] == '(':
                remove(s[::-1], 0, 0, [')', '('])
            else:
                ans.append(s[::-1])
        
        ans = []
        remove(s, 0, 0, ['(', ')'])
        return ans
```
*Optimized code:*  
```py
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def dfs(s, last, par, res):
            count = 0
            for i, ch in enumerate(s):
                if ch == par[0]:
                    count += 1
                elif ch == par[1]:
                    count -= 1
                if count >= 0:
                    continue
                for j in range(last, i+1):
                    if s[j] == par[1] and (j == last or s[j-1] != par[1]):
                        dfs(s[:j]+s[j+1:], j, par, res)
                return
            if par[0] == '(':
                if count == 0:
                    res.append(s)
                else:
                    dfs(s[::-1], 0, [')', '('], res)
            else:
                res.append(s[::-1])
        res = []
        dfs(s, 0, ['(', ')'], res)
        return res
```
*BackTracking*  
TC: O(N^2) ; SC: O(N) 
```py
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        min_remove = float('inf')
        res = set()
        
        def dfs(depth, left, right, remove, cur):
            if depth == len(s):
                if left == right:
                    nonlocal min_remove, res
                    if remove < min_remove:
                        min_remove = remove
                        res = {cur}
                    elif remove == min_remove:
                        res.add(cur)
            else:
                if s[depth] != '(' and s[depth] != ')':
                    dfs(depth+1, left, right, remove, cur+s[depth])
                else:
                    dfs(depth+1, left, right, remove+1, cur)
                    if s[depth] == '(':
                        dfs(depth+1, left+1, right, remove, cur+'(')
                    elif right < left:
                        dfs(depth+1, left, right+1, remove, cur+')')
        
        dfs(0, 0, 0, 0, '')
        return list(res)
```
*Limited Backtracking!*  
Time Complexity : The optimization that we have performed is simply a better form of pruning. Pruning here is something that will vary from one test case to another.  
  In the worst case, we can have something like ((((((((( and the left_rem = len(S) and in such a case we can discard all of the characters because all are misplaced.  
  So, in the worst case we still have 2 options per parenthesis and that gives us a complexity of O(2^N).
Space Complexity : The space complexity remains the same i.e.  
  O(N) as previous solution. We have to go to a maximum recursion depth of NN before hitting the base case.  
  Note that we are not considering the space required to store the valid expressions.  
  We only count the intermediate space here.
```py
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = 0, 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left == 0:
                    right += 1
                elif left > 0:
                    left -= 1
        res = set()
        
        def dfs(depth, left, right, left_ram, right_ram, cur):
            if depth == len(s):
                nonlocal res
                if left_ram == right_ram == 0:
                    res.add(cur)
            else:
                if s[depth] == '(' and left_ram > 0:
                    dfs(depth+1, left, right, left_ram-1, right_ram, cur)
                if s[depth] == ')' and right_ram > 0:
                    dfs(depth+1, left, right, left_ram, right_ram-1, cur)
                if s[depth] != '(' and s[depth] != ')':
                    dfs(depth+1, left, right, left_ram, right_ram, cur+s[depth])
                elif s[depth] == '(':
                    dfs(depth+1, left+1, right, left_ram, right_ram, cur+'(')
                elif s[depth] == ')' and left > right:
                    dfs(depth+1, left, right+1, left_ram, right_ram, cur+')')
        
        dfs(0, 0, 0, left, right, '')
        return list(res)
```
**2.BFS**  
```py
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def isValid(s):
            c = 0
            for p in s:
                if p == '(': c += 1
                if p == ')': c -= 1
                if c < 0: return False
            return c == 0
        
        level = {s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            else:
                level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
```
