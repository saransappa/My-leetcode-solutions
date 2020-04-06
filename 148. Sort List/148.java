/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        PriorityQueue <Integer> minHeap = new PriorityQueue();
        while(head!=null){
            minHeap.add(head.val);
            head = head.next;
        }
        ListNode dummy = new ListNode(-1);
        ListNode temp = dummy;
        while(!minHeap.isEmpty()){
            temp.next = new ListNode(minHeap.poll());
            temp = temp.next;
        }
        return dummy.next;
    }
}