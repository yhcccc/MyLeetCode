1.
```py
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        i = 0
        res = ''
        bnum = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        Roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        while num != 0:
            if num >= bnum[i]:
                res += Roman[i]
                num = num - bnum[i]
            else:
                i += 1
        return res
```
2.
```py
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        map = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        n = len(s)
        for i in range(n-1):
            if map[s[i]] >= map[s[i + 1]]:
                res += map[s[i]]
            else:
                res -= map[s[i]]
        res += map[s[n-1]]
        return res
        
```

