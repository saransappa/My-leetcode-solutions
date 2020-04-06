/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null){
            return head;
        }
        ListNode temp = head;
        ListNode prev = head;
        int count=0;
        while(temp!=null){
            temp=temp.next;
            count++;
        }
        
        
        if(k>count){
            k= (int)(k%count);
        }
        
        temp=head;
        for(int i=0;i<k;i++){
            temp = head;
            prev = head;
            while(temp.next!=null){
                prev =temp;
                temp=temp.next;
            }
            temp.next = head;
            head = temp;
            prev.next = null;
        }
        return head;
    }
}