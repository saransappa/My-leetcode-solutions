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
    String s1 = "";
    public boolean isValidBST(TreeNode root) {
        if(root == null){
            return true;
        }
        else{
            inorder(root);
            String s2="";
            for(int i=0;i<s1.length()-1;i++){
                s2+=s1.charAt(i);
            }
            String [] arr = s1.split(" ");
            int [] a = new int[arr.length];
            for(int i=0;i<arr.length;i++){
                a[i] = Integer.parseInt(arr[i]);
            }
            int [] b = new int[a.length];
            for(int i=0;i<a.length;i++){
                b[i]=a[i];
            }
            Arrays.sort(a);
          
            for(int i=0;i<a.length;i++){
                if(i+1<a.length && a[i]==a[i+1]){
                    return false;
                }
                if(a[i]!=b[i]){
                    return false;
                }
            }
            return true;
        }
        
    }
    public void inorder(TreeNode temp){
        if(temp.left!=null){
            inorder(temp.left);
        }
        s1+=temp.val+" ";
        if(temp.right!=null){
            inorder(temp.right);
        }
    }
}