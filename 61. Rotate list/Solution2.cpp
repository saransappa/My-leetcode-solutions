/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL || head->next==NULL)return head;
        int c= 0;
        ListNode* z = head;
        while(z!=NULL){
            z = z->next;
            c++;
        }
        k = k%c;
        for(int i=0;i<k;i++){
            ListNode* last = head;
            while(last->next->next!=NULL)last = last->next;
            last -> next ->next= head;
            head = last -> next ;
            last -> next = NULL;
        }   
        return head;
    }
};