**1.Recursive Approach**  
```py
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root != None:
            if root.left != None:
                self.helper(root.left, res)
            res.append(root.val)
            if root.right != None:
```
**2.Iterating method using Stack**  
```py
class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        curN = root
        while curN is not None or stack:
            while curN is not None:
                stack.append(curN)
                curN = curN.left
            curN = stack.pop()
            res.append(curN.val)
            curN = curN.right
        return res
```
**3.Morris Traversal**  
[Threaded binary tree](https://en.wikipedia.org/wiki/Threaded_binary_tree) and [Explaination of morris method](https://stackoverflow.com/questions/5502916/explain-morris-inorder-tree-traversal-without-using-stacks-or-recursion)  
```py
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        curN = root
        while curN is not None:
            if curN.left is None:
                res.append(curN.val)
                curN = curN.right
            else:
                pre = curN.left
                while pre.right is not None:
                    pre = pre.right
                pre.right = curN
                temp = curN
                # original curN left be null, avoid infinite loops
                curN = curN.left
                temp.left = None
        return res
```
