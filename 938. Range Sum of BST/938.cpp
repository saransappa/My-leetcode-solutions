/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sum = 0;
    int low_ = 0, high_ = 0;
    int rangeSumBST(TreeNode* root, int low, int high) {
        low_ = low;
        high_ = high;
        inorder(root);
        return sum;
    }
    void inorder(TreeNode* root){
        if(root->left!=NULL)inorder(root->left);
        int k = root->val;
        if(k>=low_ && k<=high_)sum+=k;
        if(root->right!=NULL)inorder(root->right);
        
    }
    
};