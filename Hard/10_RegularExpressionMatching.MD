--------------------------
**1.Recursion**(failed)  
```py
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s
        FirstMatch = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            # '*' Matches zero or more of the preceding element.
            return self.isMatch(s, p[2:]) or FirstMatch and self.isMatch(s[1:], p)
        else:
            return FirstMatch and self.isMatch(s[1:], p[1:])
```
---------------------------
**2.DP(Top-Down Variation)**  
dp(i, j): does text[i:] and pattern[j:] match?  
Key:Set a 2-D parameters's hash map by tuple.
```py
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dpdict = {}
        def dp(i, j):
            if (i, j) not in dpdict:
                if j == len(p):
                    ans = i == len(s)
                else:
                    flag = i < len(s) and p[j] in {s[i], '.'}
                    if j < len(p) - 1 and p[j+1] == '*':
                        ans = dp(i, j+2) or flag and dp(i+1, j)
                    else:
                        ans = flag and dp(i+1, j+1)
                dpdict[i, j] = ans
            return dpdict[i, j]
        return dp(0, 0)
```
-------------------------
**3.DP(Bottom-Up Variation, reverse = True)**  
dp(i, j): does text[i:] and pattern[j:] match?  
```py
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Bottom-Up Variation
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                flag = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or flag and dp[i + 1][j]
                elif flag:
                    dp[i][j] = dp[i + 1][j + 1]
        return dp[0][0]
```
--------------------------
**4.DP(Bottom-Up Variation, reverse = False)**  
Differently, dp(i, j) denotes if s[:i] and p[:j] match.  
```py
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        # This loop make sure that 'c' at the beginning of 'p' could be Correct judged
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                if i >= 2:
                    dp[0][i] = dp[0][i - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*': 
                    # '*' Matches zero or more of the preceding element.
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
                elif p[j - 1] in {s[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]
```
-----------------------------
**5.Excellent answer(just copy)**  
```py
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if (len(p) - (2*p.count('*'))) > len(s):
            return False
        
        dp0 = [False for i in range(len(s)+1)]
        dp0[0] = True
        
        i = 0
        
        while i < len(p):
            dp1 = [False for k in range(len(s)+1)]
            
            if p[i] == '.':
                if (i<len(p)-1) and p[i+1] == '*':
                    dp1[0] = dp0[0]
                    for j in range(1, len(dp0)):
                        dp1[j] = dp0[j] or dp1[j-1]
                    i += 1
                else:
                    for j in range(1, len(dp0)):
                        dp1[j] = dp0[j-1]
            else:
                if (i<len(p)-1) and p[i+1] == '*':
                    dp1[0] = dp0[0]
                    for j in range(1, len(dp0)):
                        dp1[j] = dp0[j] or (dp1[j-1] and (s[j-1]==p[i]))
                    i += 1
                else:
                    for j in range(1, len(dp0)):
                        dp1[j] = dp0[j-1] and (s[j-1]==p[i])
                
            
            i += 1
            dp0 = dp1
        
        return dp0[-1]
```
