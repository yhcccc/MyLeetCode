----------------
### 102
**BFS**  
```py
def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans
```

**DFS**  
```py
def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        self.levelhelper(res, root, 0)
        return res
    
    def levelhelper(self, res, root, height):
        if root is None: return
        if height >= len(res):
            res.append([])
        
        res[height].append(root.val)
        self.levelhelper(res, root.left, height + 1)
        self.levelhelper(res, root.right, height + 1)
```

----------
### 103.Zigzag
**BFS**  
```py
def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
    if not root: return []
    res = []
    temp, stack, flag = [], [root], 1
    while stack:
        temp = []
        for i in range(len(stack)):
            node = stack.pop(0)
            temp.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        res.append(temp[::flag])
        flag *= -1
    return res
```

**DFS**  
```py
def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
    res = []
    self.levelhelper(res, root, 0)
    return res

def levelhelper(self, res, root, height):
    if root is None: return
    if height >= len(res):
        res.append([])

    if height % 2 == 0:
        res[height].append(root.val)
    else:
        res[height] = [root.val] + res[height]
    self.levelhelper(res, root.left, height + 1)
    self.levelhelper(res, root.right, height + 1)
```
