-------------------------
**1.Stack**  
Based on the previous parenthesis problem, we need to add -1 to the bottom of the stack when dealing with this problem.  
We calculate 'length = i - l[-1](peak of stack)' to update 'lmax' everytime the stack is not empty after impelementing poping.  
Otherwise, we push s[i] into the stack in case the stack is empty.
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
See <https://leetcode.com/problems/longest-valid-parentheses/solution/>  
```py
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l < 2:
            return 0
        dp = [0 for i in range(l)]
        for i in range(1, l):
            if s[i] == ')':
                # Condition 1
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                # Condition 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
        return max(dp)
```
