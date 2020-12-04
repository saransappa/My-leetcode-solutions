# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        k = ''
        l = ''
        while l1!=None:
            k+=str(l1.val)
            l1 = l1.next
            
        while l2!=None:
            l+=str(l2.val)
            l2 = l2.next
        z = str(int(k)+int(l))
        head = ListNode(-1)
        temp = head
        for i in range(len(z)):
            temp.next = ListNode(int(z[i]))
            temp = temp.next
        return head.next