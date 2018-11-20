1.层序遍历
```py
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        acc = [e for e in d[digits[0]]] # 必须将acc初始化为非空列表，否则循环中acc将始终为空列表
        for digit in digits[1:]:
            acc = [w1 + w2 for w1 in acc for w2 in d[digit]]
        return acc
```
