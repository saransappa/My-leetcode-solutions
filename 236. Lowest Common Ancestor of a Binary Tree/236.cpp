/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    map<TreeNode*,TreeNode*> parent;
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        inorder(root);
        //cout<<"done"<<endl;
        parent[root]=NULL;
        set<TreeNode*> s;
        TreeNode* temp = p;
        while(temp!=NULL){
            s.insert(temp);
            temp = parent[temp];
        }
        temp = q;
        while(temp!=NULL){
            int z = s.size();
            s.insert(temp);
            if(z==s.size())return temp;
            temp = parent[temp];
        }
        return root;
    }
    
    void inorder(TreeNode* root){
        if(root->left!=NULL){
            inorder(root->left);
            parent[root->left] = root;   
        }
        //cout<<root->val<<endl;
        if(root->right!=NULL){
            inorder(root->right);
            parent[root->right] = root;    
        }
        
    }
};