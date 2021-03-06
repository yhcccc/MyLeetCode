-------------------------
### 1.正反对比，最大公共子串且index对的上
   这里引出了最大公共子串问题，使用dynamicPlanning方法，时间复杂度O(n^2),空间复杂度O(n^2)。
   可将二维数组压缩为hash表或者两行数组节省空间，暂未实现。
```py
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        
        d = [[0]*n for i in range(n)] # n*n数组
        z = 0
        ret = ''
        for i in range(n):
            for j in range(n):
                if s[i] == s[n-1-j]:
                    if i == 0 or j == 0:
                        d[i][j] = 1
                    else:
                        d[i][j] = d[i-1][j-1] + 1 #查询对角线上一个数字 
                    if d[i][j] >= z and j + i - d[i][j] + 2 == n:
                        z = d[i][j]
                        ret = s[i - z + 1 : i + 1]
        return ret
 ```
        
        
-------------------------
### 2.动态规划
  从2n-1个起点开始左右对比，2n-1是因为有奇(aba)、偶(abba)两种情况，即每1/2个字符为一个起点
```py
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        for i in range(len(s)):
            # 奇
            temp = self.dyp(s, i, i)
            if len(temp) > len(ret):
                ret = temp
            # 偶
            temp = self.dyp(s, i, i + 1)
            if len(temp) > len(ret):
                ret = temp
        return ret
        
    def dyp(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
```

-------------------------
### 3.Manacher's
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
