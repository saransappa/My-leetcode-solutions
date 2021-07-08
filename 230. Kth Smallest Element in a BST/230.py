# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.z = []
    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        self.z.append(root.val)
        if root.right!=None:
            self.inorder(root.right)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder(root)
        return self.z[k-1]