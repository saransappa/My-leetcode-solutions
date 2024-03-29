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
class BSTIterator {
    public ArrayList<Integer> arr =new ArrayList<Integer> ();
    public int pointer;
    public BSTIterator(TreeNode root) {
        inorder(root);
        pointer = -1;
    }
    
    public void inorder(TreeNode root){
        if(root.left!=null)inorder(root.left);
        arr.add(root.val);
        if(root.right!=null)inorder(root.right);
    }
    
    public int next() {
            pointer++;
            return arr.get(pointer); 
    }
    
    public boolean hasNext() {
        if(pointer == -1 && arr.size()>0)return true;
        else if(pointer+1<arr.size())return true;
        else return false;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */