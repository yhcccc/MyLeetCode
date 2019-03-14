**Backtrack**
```py
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtrack([], res, s)
        return res
        
    def backtrack(self, temp, res, s):
        if len(s) == 0:
            res.append(temp)
            return
        for j in range(1, len(s)+1):
            s_clip = s[:j]
            if s_clip == s_clip[::-1]:
                self.backtrack(temp+[s_clip], res, s[j:])
```
