**1.onePass**  
```py
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        if l2 is None: return l1
        if l1 is None and l2 is None: return None
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        pCur = dummy
        while p1 != None and p2 != None:
            if p1.val > p2.val:
                pCur.next = p2
                p2 = p2.next
                pCur = pCur.next
            else:
                pCur.next = p1
                p1 = p1.next
                pCur = pCur.next
        if p1 == None:
            pCur.next = p2
        if p2 == None:
            pCur.next = p1
        return dummy.next
```
