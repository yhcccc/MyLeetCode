**O(n + k%n) method**  
```py
class Solution:
    def rotateRight(self, head, k):
	
        if not head or not head.next: return head
		# Create a dummy head node to simplify the code
        dummy = ListNode(0)
        dummy.next = head
        
        def Findk(dummy, Lr, k):
            for i in range(k):
                if Lr.next.next == None:
                    return Findk(dummy, dummy, k % (i + 1))
                else:
                    Lr = Lr.next
            return Lr
        
		# Find the kth or (k%n)th element from the bottom
        Lr = Findk(dummy, dummy, k)
        if Lr == dummy: return head
        Ll = dummy
        while Lr.next != None:
            Lr = Lr.next
            Ll = Ll.next
        
		# Finish the rotate
        Lr.next = dummy.next
        dummy.next = Ll.next
        Ll.next = None
        
        return dummy.next
```
