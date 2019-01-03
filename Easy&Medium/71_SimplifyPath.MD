**Stack**  
```py
class Solution:
    def simplifyPath(self, path):
        stack = []
        skip = {"", ".", ".."} # set is a hash table, which find operation is fast.
        for s in path.split("/"):
            if s == ".." and stack:
                stack.pop()
            elif not s in skip: 
                stack.append(s)
        return "/" + "/".join(stack)
```
