-------------------------
**1.Stack**  
Based on the previous parenthesis problem, we need to add -1 to the bottom of the stack when dealing with this problem.  
We calculate 'length = i - l[-1](peak of stack)' to update 'lmax' everytime the stack is not empty after impelementing poping.  
```py
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        l = [-1]
        lmax = 0
        for i,c in enumerate(s):
            if c == '(':
                l.append(i)
            else:
                l.pop()
                if l:
                    lmax = max(lmax, i - l[-1])
                else:
                    l = [i]
        return lmax
```

-------------------------
**2.DP**  
思路见<https://articles.leetcode.com/longest-palindromic-substring-part-ii/>  

```py
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # 避免边界判断
        t = '^'
        for i in range(n):
            t += ('#' + s[i])
        t += '#$'
        m = 2*n + 3
        p = [0]*m
        c = 0; r = 0
        for j in range(1,m-1):
            j_mirror = 2*c - j
            if r > j:
                p[j] = min(r - j, p[j_mirror])
            # 这里会到达边界，所以前面在字符串前后多加一个字符
            while t[j - 1 - p[j]] == t[j + 1 + p[j]]:
                p[j] += 1
            if j + p[j] > r:
                r = j + p[j]
                c = j
        l = max(p)
        center = p.index(l)
        # 删去'^'
        t = t[1:]
        return t[center - l - 1: center + l].replace('#', '')
```
