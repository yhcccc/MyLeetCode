# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

##########################################
#递归式地 先做加法，再判断以及改变
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        S = ListNode(l1.val + l2.val)
        carry = 0
        if S.val > 9:
            S.val = S.val - 10
            carry = 1
        
        if carry == 0 and l1.next is None and l2.next is None:
            return S
        else:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            l1.next.val = l1.next.val + carry
            S.next = self.addTwoNumbers(l1.next, l2.next)
            return S
			
##########################################
#循环式 一样的思路			
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        Sr = S = ListNode(0)
        while(l1 or l2):
            
            S.next = ListNode(l1.val + l2.val)
            carry = 0
            if S.next.val > 9:
                S.next.val = S.next.val - 10
                carry = 1

            if carry == 0 and l1.next is None and l2.next is None:
                break
            else:
                if l1.next is None:
                    l1.next = ListNode(0)
                if l2.next is None:
                    l2.next = ListNode(0)
                l1.next.val = l1.next.val + carry
                l1 = l1.next; l2 = l2.next
                S = S.next   
        S = Sr.next
        del Sr
        return S