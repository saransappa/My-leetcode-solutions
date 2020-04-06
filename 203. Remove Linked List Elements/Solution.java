/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if(head==null){
            return null;
        }
       
        ListNode temp =head;
        while(temp.next!=null){
            if(temp.next.val==val){
                temp.next = temp.next.next;
            }
            else{
                temp=temp.next;
            }
        }
         if(head.val ==val){
            head = head.next;
        }
        return head;
    }
}