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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root==null){
            root = new TreeNode(val);
            return root;
        }
        else{
            TreeNode temp =root;
            insert(temp,val);
            return root;
        }
    }
    public void insert(TreeNode temp, int val){
        if(temp.val < val){
            if(temp.right == null){
                temp.right = new TreeNode(val);
            }
            else{
                insert(temp.right,val);
            }
        }
        else{
            if(temp.left == null){
                temp.left = new TreeNode(val);
            }
            else{
                insert(temp.left,val);
            }
        }
    }

}