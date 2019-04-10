**Divide and conquer**  
```py
class Solution:
    def __init__(self):
        self.d = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 
                 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen",
                 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty",
                 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"}
    
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        res = ""
        next_, cur = divmod(num, 1000)
        # print(next_, cur)
        k = 0
        temp = ""
        while cur != 0 or next_ != 0:
            if next_ == 0:
                temp = self.d3toWords(cur).strip()
                # print(temp)
                cur = 0
            elif cur == 0:
                next_, cur = divmod(next_, 1000)
                k += 1
                continue
            else:
                temp = self.d3toWords(cur).strip()
                next_, cur = divmod(next_, 1000)
            
            if k == 0:
                res = temp
            elif k == 1:
                res = temp + " Thousand " + res
            elif k == 2:
                res = temp + " Million " + res
            elif k == 3:
                res = temp + " Billion " + res
            temp = ""
            k += 1
            res = res.strip()
        return res
        
    def d3toWords(self, num):
        if num == 0: return ""
        if num in self.d: return self.d[num]
        elif num < 100:
            return self.d2toWords(num)
        else:
            a, b = divmod(num, 100)
            return self.d[a] + " Hundred " + self.d2toWords(b)
        
    def d2toWords(self, num):
        if num == 0: return ""
        if num in self.d: return self.d[num]
        a, b = divmod(num, 10)
        return self.d[a*10] + " " + self.d[b]
```        
simplied:
```py
class Solution:
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n//10-2]] + words(n%10)
            if n < 1000:
                return [to19[n//100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n//1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'
```
