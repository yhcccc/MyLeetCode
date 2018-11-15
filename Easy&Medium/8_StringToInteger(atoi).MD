------------------------------------------
**1.暴力法
无需技巧，按情况判断即可
```py
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip(' ')
        if str == '':
            return 0
        res = 0
        flag = 1
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if (str[0]<'0' or str[0]>'9') and (str[0] != '-' and str[0] != '+'):
            return 0
        else:
            if str[0] == '-':
                flag = -1
            elif str[0] == '+':
                flag = 1
            else:
                res = int(str[0])
            for i in range(1,len(str)):
                if str[i] == ' ' or str[i]<'0' or str[i]>'9':
                    break
                else:
                    res = res*10 + int(str[i])
        if flag==1:
            if res <= INT_MAX:
                return res
            return INT_MAX
        else: 
            if res*flag >= INT_MIN:
                return res*flag
            return INT_MIN
```
