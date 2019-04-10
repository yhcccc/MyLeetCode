**1.PriorityQueue(MinHeap)**  
TC: O(Nlogk); SC: O(n)+O(k)
```py
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val
        dummy = ListNode(0)
        head = dummy
        heap = PriorityQueue()
        for node in lists:
            if node:
                heap.put(node)
        while not heap.empty():
            head.next = heap.get(heap)
            head = head.next
            if head.next:
                heap.put(head.next)
        return dummy.next
```
**2.Merge with Divide And Conquer**  
TC: O(Nlogk); SC: O(1)
```py
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = len(lists)
        interval = 1
        while interval < l:
            for i in range(0, l - interval, interval * 2):
                print(i)
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if l > 0 else None
        
    def merge2Lists(self, a, b):
        dummy = head = ListNode(0)
        while a and b:
            if a.val > b.val:
                head.next = b
                b = b.next
            else:
                head.next = a
                a = a.next
            head = head.next
        if a:
            head.next = a
        elif b:
            head.next = b
        return dummy.next
```
