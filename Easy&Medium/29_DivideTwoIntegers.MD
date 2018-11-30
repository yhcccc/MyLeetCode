--------------------------
**1.bit manipulations**  
It will produce some repetitive calculations.
```py
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        Int_Max = 2147483647; Int_Min = -2147483648
        if not divisor or (dividend == Int_Min and divisor == -1):
            return Int_Max
        sign = 0 if (dividend > 0) ^ (divisor > 0) else 1
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        while a >= b:
            temp = b; mul = 1
            while a >= (temp << 1):
                temp <<= 1
                mul <<= 1
            a -= temp
            res += mul
        return res if sign else -res        
```
-----------------------------
**2.32 times bit shift operation in C with O(1) solution**  
```py
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        Int_Max = 2147483647; Int_Min = -2147483648
        if not divisor or (dividend == Int_Min and divisor == -1):
            return Int_Max
        sign = not ((dividend > 0) ^ (divisor > 0))
        a = dividend if dividend > 0 else -dividend
        b = divisor if divisor > 0 else -divisor
        ret = 0
        for i in range(31, -1, -1):
            if (a>>i) >= b:
                ret <<= 1
                ret += 1
                a -= (b<<i)
            else:
                ret <<= 1
        return ret if sign else -ret
            
```
