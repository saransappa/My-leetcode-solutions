/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        int k;
        if(root==null){
            return 0;
        }
        else{
            k = inorder(root,0);
        }
        return k;
    }
    
    public int inorder(TreeNode root,int x){
        if(root.left!=null){
            if(root.left.left==null && root.left.right==null)
            x+=root.left.val;
            x = inorder(root.left,x);
        }
        //System.out.println(x);
        if(root.right!=null){
            x = inorder(root.right,x);
        }
        return x;
    }
}