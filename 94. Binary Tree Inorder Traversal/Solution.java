/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.*;
class Solution {
    int k=0;
    List<Integer> list = new ArrayList();
    public void visit(TreeNode temp){
        if(temp!=null){
            list.add(k,temp.val);
            k++;
        }
    }
    public void inorder(TreeNode root){
        if(root == null){
            return;
        }
        else{
            inorder(root.left);
            visit(root);
            inorder(root.right);
        }
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root == null){
            List <Integer> k = new ArrayList();
            return k;
        }
        inorder(root);
        return list;
    }
}