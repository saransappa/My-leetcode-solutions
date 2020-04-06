/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int max(int a,int b){
        if(a>b){
            return a;
        }
        else{
            return b;
        }
    }
    public int findHeight(TreeNode root){
        if(root == null){
            return 0;
        }
        else{
            int leftHeight= findHeight(root.left);
            int rightHeight = findHeight(root.right);
            return max(leftHeight,rightHeight)+1;
        }
    }
    public int maxDepth(TreeNode root) {
        return findHeight(root);
    }
}