1.Stack  
Time complexity : O(n)  
Space complexity : O(n)
```py
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')':'(', '}':'{', ']':'['}
        l = []
        for w in s:
            
            if w in d:
                top = l.pop() if l else '#'
                if d[w] != top:
                    return False
                
            else:
                l.append(w)
        return not l
```
