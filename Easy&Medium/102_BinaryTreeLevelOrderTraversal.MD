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
