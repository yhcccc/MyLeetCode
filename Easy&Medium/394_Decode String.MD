**Stack**
```py
class Solution:
    def decodeString(self, s: str) -> str:
        queue = []
        num, cur = '', ''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                n = int(num)
                queue.append([n, cur])
                cur = ''
                num = ''
            elif ch == ']':
                n, pre = queue.pop()
                cur = pre + n * cur
            else:
                cur += ch
        del queue
        return cur
```
