---------------------------------------------------------  
  
**字符串切片**
利用python语言优势，将int转为Str，再作逆序变换即可，注意正负号。    
```py
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        a = str(x)
        b = int(a[::-1]) if x > 0 else -int(a[:0:-1])
        return b if b < 2**31 - 1 and b > -2**31 else 0
```
