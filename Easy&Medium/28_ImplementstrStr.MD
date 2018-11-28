#### Although it's a easy problem, it is necessary to delve into it.  
-----------------
**1.The advantage of python**  
```py
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i : i+len(needle)] == needle:
                return i
        return -1
```
-----------------
**2.KMP Algorithm**  
Learn KMP <https://blog.csdn.net/v_july_v/article/details/7041827>
```py
class Solution:
    def kmpNext(self, p):
        l = len(p)
        Next = [0 for i in range(l)]
        Next[0] = -1
        k = -1; j = 0
        while(j < l - 1):
            if k == -1 or p[j] == p[k]:
                k += 1
                j += 1
                if p[j] != p[k]:
                    Next[j] = k
                else:
                    Next[j] = Next[k]
            else:
                k = Next[k]
        return Next
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        lh = len(haystack)
        ln = len(needle)
        i = 0; j = 0
        Next = self.kmpNext(needle)
        while i < lh and j < ln:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = Next[j]
        if j == ln:
            return i - j
        else:
            return -1
```
------------------ 
**3.BM Algorithm**  
Also see in <https://blog.csdn.net/v_july_v/article/details/7041827>  
            <https://blog.csdn.net/frostime/article/details/78294658>
```py

```
------------------
**4.Sunday Algorithm** 
Also see in <https://blog.csdn.net/v_july_v/article/details/7041827>  
            <https://blog.csdn.net/q547550831/article/details/51860017>
```py
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        ln = len(needle)
        i = 0
        while i < len(haystack):
            if haystack[i: i + ln] == needle:
                return i
            else:
                index = 0
                try:
                    index = needle.rindex(haystack[i + ln])
                except Exception:
                    i += ln + 1
                i += ln - index
        return -1
```
