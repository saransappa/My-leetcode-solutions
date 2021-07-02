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
    ArrayList <Integer> arr = new ArrayList<Integer> ();
    public boolean isValidBST(TreeNode root) {
        if(root==null)return true;
        else{
            check(root);
            for(int i=0;i<arr.size()-1;i++){
                if(arr.get(i)>=arr.get(i+1))return false;
            }
            return true;
        }
    }
    public boolean check(TreeNode root){
        if(root.left!=null)check(root.left);
        arr.add(root.val);
        if(root.right!=null)check(root.right);
        return true;
    }
}