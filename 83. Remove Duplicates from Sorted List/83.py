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
        k = set(k)
        k = list(k)
        k.sort()
        temp2 = ListNode(-1)
        temp = temp2
        for i in range(len(k)):
            temp.next = ListNode(k[i])
            temp = temp.next
        return temp2.next