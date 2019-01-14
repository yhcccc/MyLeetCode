**DP**  
My Codes:
```py
class Solution:
    def numDecodings(self, s):
        dp = [1 for _ in range(len(s))]
        if s[0] == '0':
            dp[0] = 0
        flag = 0
        for i in range(1, len(s)):
            if s[i] != '0':
                flag_pre = flag
                flag = 0
                if s[i-1] != '0' and int(s[i-1:i+1]) < 27:
                # also written as: if 9 < int(s[i-1:i+1]) < 27:
                    flag = 1
                dp[i] = dp[i-1] + flag * dp[i-1] - flag_pre * flag * dp[i-3]
                # Key: dp[i] = dp[i-1] + dp[i-2]*flag; My codes are complicated.
            else:
                if int(s[i-1]) > 2 or s[i-1] == '0':
                    dp[i] = 0
                else:
                    dp[i] = dp[i-2]
        return dp[-1]
```
A amazing simplified version by @StefanPochmann:  
```py
class Solution:
    def numDecodings(self, s):
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, w * (d>'0') + v * (9<int(p+d)<27), d
        return w
```
