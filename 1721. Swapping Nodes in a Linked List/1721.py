# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        a = []
        while head!=None:
            a.append(head.val)
            head = head.next
        temp = a[k-1]
        a[k-1] = a[len(a)-k]
        a[len(a)-k] = temp
        
        head = ListNode(a[0])
        t = head
        for i in range(1,len(a)):
            t.next = ListNode(a[i])
            t = t.next
        return head
        