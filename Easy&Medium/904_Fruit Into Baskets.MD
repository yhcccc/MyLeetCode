*1.Scan Through Blocks*  
TC:  O(N); SC: O(N)
```py
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        block = [0]
        for i in range(1, len(tree)):
            if tree[i] != tree[i-1]:
                block.append(i)
        block.append(len(tree))
        i = 0
        res = 0
        while i < len(tree):
            weight = 0
            Set = set()
            for j in range(i, len(block)-1):
                Set.add(tree[block[j]])
                weight += block[j+1] - block[j]
                if len(Set) > 2:
                    i = j - 1
                    break
                res = max(res, weight)
            else: break
        return res 
```

*2.Sliding Window*  
TC:  O(N); SC: O(N)  
```py
from collections import Counter
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = 0
        i = 0
        count = Counter()
        for j, f in enumerate(tree):
            count[f] += 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res 
```

*3.Longest Subarray With 2 Elements*  
<https://leetcode.com/problems/fruit-into-baskets/discuss/170745/Problem%3A-Longest-Subarray-With-2-Elements>
```py
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = 0
        cur, pre, curCount, preCount = -1, -1, 0, 0
        for i in range(len(tree)):
            if tree[i] != cur and tree[i] != pre:
                pre = cur
                cur = tree[i]
                preCount = curCount
                curCount = 1
            elif tree[i] == cur:
                curCount += 1
            else:
                cur, pre = pre, cur
                preCount += curCount
                curCount = 1
            res = max(res, preCount + curCount)
        return res
```
