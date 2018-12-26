**1.Categorize by Sorted String**  
Time Complexity: O(NK*logK);Space Complexity: O(NK)
```py
class Solution:
    def groupAnagrams(self, strs):
        d = {}
        res = []
        n = 0
        for s in strs:
            sl = list(s)
            sl.sort()
            st = tuple(sl)
            if st in d:
                res[d[st]].append(s)
            else:
                d[st] = n
                res.append([s])
                n += 1
        return res
```
Optimized Version as below  
```py
class Solution():
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())
```
**2.Categorize by Count**  
Time Complexity: O(NK);Space Complexity: O(NK)
```py
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
```
