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
    String s1="";
    public void visit(TreeNode t){
            s1+=t.val;
    }
    public void inorder(TreeNode t){
        if(t==null){
            s1+="N";
            return;
        }
        else{
            inorder(t.left);
            visit(t);
            inorder(t.right);
        }
    }
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q==null){
            return true;
        }
        if((p==null && q!=null ) || (p!=null && q==null)){
            return false;
        }
        if(p.val != q.val){
            return false;
        }
        if(p.val==q.val && p.left==null && q.left == null && p.right==null && q.right ==null){
                return true;
        }
        if((p.left == null && q.left!=null)||(p.left!=null && q.left==null)){
            return false;
        }
        //s1= "";
        inorder(p);
        s1+="  ";
        inorder(q);
        System.out.println(s1);
        if(s1.length()>1){
            String [] arr = s1.split("  ");
            if(arr[0].equals(arr[1])){
                return true;
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }
    }
}