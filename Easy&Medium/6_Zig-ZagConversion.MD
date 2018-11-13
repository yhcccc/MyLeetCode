-----------------------------------------------------
##1.按行遍历    
z字行序列的循环周期序列，周期为```T=2*numRows-2```;若遍历到第i行，在第j(0开始)个循环，斜线上的字符index为```i+T-2i+T*j=(j+1)*T-i```.  
*代码中的j为此处的```j*T```
```py
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        ret = ''
        n = len(s)
        cycleLen = 2 * numRows - 2

        for i in range(numRows):
            for j in range(0, n - i, cycleLen):
                ret += s[j + i]
                if i != 0 and i != numRows - 1 and j + cycleLen - i < n: #第一行和最后一行无斜线字符
                    ret += s[j + cycleLen - i]
            
        return ret
```

-----------------------------------------------------
##2.按s遍历    
只用建立一个长度为numRows的list,通过goingDown判断填入list的方向即可。  
```py
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        rows = min(numRows, len(s))
        l = ['']*(rows) # list初始化时务必给定参数类型，否则空list会在赋值时报错
        goingDown = False
        curRow = 0
        for c in s:
            l[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown #改变方向
            curRow += 1 if goingDown else -1
            
        return "".join(l)
```
