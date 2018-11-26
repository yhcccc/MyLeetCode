---------------------------------
To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next,   
we need to change those three references.  
Instead of thinking about in what order I change them, I just change all three at once.  
```py
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = dummy = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return dummy.next
```
It may be faster written as follows.
```py
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = dummy = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            temp = b.next
            pre.next = b
            b.next = a
            a.next = temp
            pre = a
        return dummy.next
```
We can also go from pre -> a -> b -> c -> d -> d.next to pre -> b -> a -> d -> c -> c.next.  
But it seems to cost the same amount of time.
```py
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = dummy = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            if b.next and b.next.next:
                c = b.next
                d = c.next
                temp = d.next
                pre.next = b
                b.next = a
                a.next = d
                d.next = c
                c.next = temp
                pre = c
            else:
                temp = b.next
                pre.next = b
                b.next = a
                a.next = temp
                pre = a
        return dummy.next
```
