# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        k = ""
        l = ""
        while l1!=None:
            k += str(l1.val)
            l1 = l1.next
        while l2!=None:
            l += str(l2.val)
            l2 = l2.next
        k = k[::-1]
        l = l[::-1]
        p = int(k)+int(l)
        p = str(p)
        p = p[::-1]
        h = ListNode()
        z = h
        for i in range(len(p)):
            h.val = int(p[i])
            if i == len(p)-1:
                h.next = None
            else:
                h.next = ListNode()
            h = h.next
        return z