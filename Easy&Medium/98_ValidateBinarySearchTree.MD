<https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)>  
**1.Recursion**  
```py
class Solution:
    def isValidBST(self, root):
        if not root: return True
        def isBSTHelper(node, lower_limit, upper_limit):
            if lower_limit is not None and node.val <= lower_limit:
                return False
            if upper_limit is not None and node.val >= upper_limit:
                return False
            left = isBSTHelper(node.left, lower_limit, node.val) if node.left else True
            if left:
                right = isBSTHelper(node.right, node.val, upper_limit) if node.right else True
                return right
            else:
                return False
        return isBSTHelper(root, None, None)
```
**2.iteration(stack)**  
```py
class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        
        stack = [(root, None, None), ]
        while stack:
            root, lower_limit, upper_limit = stack.pop()
            if root.right:
                if root.right.val > root.val:
                    if upper_limit and root.right.val >= upper_limit:
                        return False
                    stack.append((root.right, root.val, upper_limit))
                else:
                    return False
            if root.left:
                if root.left.val < root.val:
                    if lower_limit and lower_limit >= root.left.val:
                        return False
                    stack.append((root.left, lower_limit, root.val))
                else:
                    return False
        return True
```
```py
class Solution:
    def isValidBST(self, root):
        if not root: return True
        pre = None
        stack = []
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre is not None and pre.val >= root.val:
                return False
            pre = root
            root = root.right
        return True
```
