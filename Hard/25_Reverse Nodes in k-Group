**1.Stack**
```py
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        queue = []
        Dummy = ListNode(-1)
        Dummy.next = head
        begin = Dummy
        while head:
            i = 0
            while i != k:
                queue.append(head)
                if head:
                    head = head.next
                else:
                    return Dummy.next
                i += 1
            begin.next = queue[-1]
            while queue:
                cur = queue.pop()
                if queue:
                    cur.next = queue[-1]
                else:
                    cur.next = head
            begin = cur
        return Dummy.next
```
**2.Recursive**  
Slower
```py
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        i = 0
        curr = head
        while curr and i != k:
            curr = curr.next
            i += 1
        
        if i == k:
            curr = self.reverseKGroup(curr, k)
            while i > 0:
                i -= 1
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
            head = curr
        return head`
```
**3.Reverse**  
General listnode reversing method: LeetCode 206
```py
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        def reverse(begin, end):
            pre = begin
            curr = begin.next
            first = curr
            while curr != end:
                Next = curr.next
                curr.next = pre
                pre = curr
                curr = Next
            begin.next = pre
            first.next = end
            return first
        
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        begin = dummy
        i = 0
        while head:
            i += 1
            if i % k == 0:
                # Begin is the former(prev) of the end, as well as the begin of the next group.
                begin = reverse(begin, head.next)
                head = begin.next
            else:
                head = head.next
        return dummy.next
```
