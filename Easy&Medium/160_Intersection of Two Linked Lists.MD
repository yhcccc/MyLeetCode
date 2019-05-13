```py
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        a = headA; b = headB
        
        while a != b:
            # the most amazing key
            a = headB if a is None else a.next
            b = headA if b is None else b.next
            
        return a
```
