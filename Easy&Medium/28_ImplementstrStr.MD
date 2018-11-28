#### Although it's a easy problem, it is necessary to delve into it.  
------------------
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
------------------
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
                    Next[j] = Next[k] # abcabc -> -1,0,0,-1,0,0. Increase movement
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
Also see in <https://blog.csdn.net/v_july_v/article/details/7041827> and  
            <https://blog.csdn.net/frostime/article/details/78294658>
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
        lh = len(haystack); ln = len(needle)
        gs = self.getGs(ln, needle)
        # Get BC table(simplified)
        bc = {}
        for i in range(ln):
            bc[needle[i]] = i
        # needle's position in haystack
        patAt = 0 
        patLastID = ln - 1
        
        while(patAt + ln <= lh):
            # cmp denotes the position in needle compared now
            cmp = patLastID
            # patAt + cmp denotes the position in haystack compared now
            while(cmp >= 0 and needle[cmp] == haystack[patAt + cmp]):
                cmp -= 1
            # cmp == -1 when Successful match occurs. 
            if cmp == -1:
                break
            else:
                # max(good index rule, bad index rule)
                # when haystack[patAt + cmp] in bc, move to the far right.
                # otherwise, move to the badID's next 
                try:
                    patAt += max(gs[cmp], cmp - bc[haystack[patAt + cmp]])
                except:
                    patAt += max(gs[cmp], cmp + 1)
        return patAt if patAt + ln <= lh else -1
    
    def Suffix(self, lp, p):
        # Suff[i] indicates the maximum length that matches the pattern string suffix with i as the boundary.
        suff = [0 for i in range(lp)]
        suff[lp - 1] = lp
        i = lp - 2
        while i >= 0:
            num = 0
            while num <= i and p[i - num] == p[lp - num - 1]:
                num += 1
            suff[i] = num
            i -= 1
        return suff
    
    def getGs(self, lp, p):
        lastID = lp - 1
        suff = self.Suffix(lp, p)
        gs = [0 for i in range(lp)]
        # no match
        for i in range(lp):
            gs[i] = lp
        # suffix
        for i in range(lastID, -1, -1):
            if suff[i] == i + 1:
                for j in range(0, lastID - i):
                    if gs[j] == lp:
                        gs[j] = lastID - i
        # the match substring in the middle
        for i in range(0, lastID):
            gs[lastID - suff[i]] = lastID - i
        return gs
    
```
------------------
**4.Sunday Algorithm**  
Also see in <https://blog.csdn.net/v_july_v/article/details/7041827> and   
            <https://blog.csdn.net/q547550831/article/details/51860017>  
Version with cheating
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
            # A cheat
            if haystack[i: i + ln] == needle:
                return i
            else:
                index = 0
                try:
                    index = needle.rindex(haystack[i + ln])
                except Exception:
                    i += ln + 1
                else:
                    i += ln - index
        return -1
```
Full Version
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
        lh = len(haystack); ln = len(needle)
        # set a shift hash map for needle
        shift = {}
        for i in range(ln):
            shift[needle[i]] = ln - i
        
        s = 0
        while(s <= lh - ln):
            j = 0
            while(haystack[s + j] == needle[j]):
                j += 1
                if j >= ln:
                    return s
            try:
                s += shift[haystack[s + ln]]
            except:
                s += (ln + 1)
        return -1
```
