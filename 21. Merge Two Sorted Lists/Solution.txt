/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        }
        else if(l2 ==null){
            return l1;
        }
        int [] array = new int[1000];
        ListNode temp1= l1;
        ListNode temp2= l2;
        int i =0;
        while(temp1!=null){
            array[i]=temp1.val;
            temp1=temp1.next;
            i++;
        }
        while(temp2!=null){
            array[i]=temp2.val;
            temp2=temp2.next;
            i++;
        }
        for(int j=i;j<1000;j++){
            array[j]=-99999;
        }
        Arrays.sort(array);
        int k =-99999;
        for(i=0;i<1000;i++){
            if(array[i]!=-99999){
                k=array[i];
                break;
            }
        }
        ListNode head = new ListNode(k);
        ListNode t = head;
        for(int j=i+1;j<1000;j++){
            if(array[j]!=-99999){
                ListNode newnode= new ListNode(array[j]);
                t.next = newnode;
                t= newnode;
            }
        }
        return head;
    }
}