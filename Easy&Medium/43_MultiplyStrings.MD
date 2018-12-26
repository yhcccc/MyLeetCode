
```py
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1); l2 = len(num2)
        pos = [0 for _ in range(l1 + l2)]
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                a, b = ord(num1[i]) - ord('0'), ord(num2[j]) - ord('0')
                p1, p2 = i + j, i + j + 1
                mul = a * b
                sum = mul + pos[p2]
                
                pos[p1] += sum // 10
                pos[p2] = sum % 10
        res = ''
        for num in pos:
            if not (res == '' and num == 0):
                res += str(num)
        return res if res else '0'
```
