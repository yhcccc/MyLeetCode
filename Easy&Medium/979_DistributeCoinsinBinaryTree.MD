**DFS**  
Algorithm  
Let dfs(node) be the excess number of coins in the subtree at or below this node:  
namely, the number of coins in the subtree, minus the number of nodes in the subtree.  
Then, the number of moves we make from this node to and from its children is abs(dfs(node.left)) + abs(dfs(node.right)).  
After, we have an excess of node.val + dfs(node.left) + dfs(node.right) - 1 coins at this node.
```py
class Solution:
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(T):
            if not T: return 0
            L, R = dfs(T.left), dfs(T.right)
            self.ans += abs(L) + abs(R)
            return T.val + L + R - 1
        
        dfs(root)
        return self.ans
```
