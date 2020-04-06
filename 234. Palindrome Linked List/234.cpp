/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> v;
        while(head!=NULL){
            v.push_back(head->val);
            head = head->next;
        }
        cout<<v.size();
        int i=0,j=v.size()-1;
        while(i<=j){
            if(v.at(i)!=v.at(j)){return false;}
            i++;
            j--;
        }
        return true;
    }
};