[Key idea](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/)  
**Recursion**
```py
class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        def helper(idx_l = 0, idx_r = len(inorder)):
            nonlocal idx_cur
            if idx_l == idx_r: return None
            
            root_val = preorder[idx_cur]
            root = TreeNode(root_val)
            
            idx_root = inorder.index(root_val)
            
            idx_cur += 1
            root.left = helper(idx_l, idx_root)
            root.right = helper(idx_root + 1, idx_r)
            return root
        idx_cur = 0
        return helper()
```
Simplified:
```py
class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root
```
