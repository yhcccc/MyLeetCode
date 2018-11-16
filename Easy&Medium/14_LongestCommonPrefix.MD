1.O(M*N)
```py
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        com = min(strs)
        lmin = len(com)
        for i, s in enumerate(com):
            for other in strs:
                if other[i] != s:
                    return com[:i]
        return com
```

2.O(L),空间更多
```py
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        com = min(strs)
        lmin = len(com)
        for i in range(lmin,-1,-1):
            if len(set(j[:i] for j in strs)) == 1:
                return com[:i]
        return ''
```
