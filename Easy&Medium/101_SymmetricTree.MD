**1.Recursion**  
O(n)  
```py
class Solution:
    def isSymmetric(self, root):
        if root == None: return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, t1, t2):
        if t1 == None and t2 == None: return True
        if t1 == None or t2 == None: return False
        return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
```

**2.Iteration(Stack)**  
```py
class Solution:
    def isSymmetric(self, root):
        if not root: return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            t1 = stack.pop()
            t2 = stack.pop()
            if not t1 and not t2: continue
            if not t1 or not t2: return False
            if t1.val != t2.val: return False
            stack.extend([t1.left, t2.right, t1.right, t2.left])
        return True
```
