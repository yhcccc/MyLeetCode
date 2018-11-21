-------------------------------------
**1.Two Pass**   
Add dummy Node before the headNode to simplify some corner cases such as a list with only one node, or removing the head of the list.  
TimeCom:O(n)  
```py
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        Lcur = head
        i = 0
        while Lcur != None:
            Lcur = Lcur.next
            i += 1
        l = i
        ndel = l - n
        Lpre = dummy
        for _ in range(ndel):
            Lpre = Lpre.next
        Lpre.next = Lpre.next.next
        return dummy.next
```  
------------------------------------- 
**2.One Pass**   
TimeCom:O(n)  
```py
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        Ll = dummy
        Lr = dummy
        for _ in range(n+1):
            Lr = Lr.next
        while Lr != None:
            Lr = Lr.next
            Ll = Ll.next
        Ll.next = Ll.next.next
        return dummy.next
```
------------------------------------- 
**3.Special method**   
TimeCom:O(n)  
```py
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list_ = []
        while head != None:
            list_ += [head.val]
            head = head.next 
        del list_[-n]
        # List in py3 is a type of LinkList.
        return list_
```
