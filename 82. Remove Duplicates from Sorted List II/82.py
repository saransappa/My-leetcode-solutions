# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head
        k = []
        while temp!=None:
            k.append(temp.val)
            temp = temp.next
        p = []
        for i in k:
            if k.count(i)>1:
                p.append(i)
        for i in p:
            while i in k:
                k.remove(i)
        temp2 = ListNode(-1)
        temp = temp2
        for i in k:
            temp.next = ListNode(i)
            temp = temp.next
        return temp2.next