# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, l):
        if root==None:
            return l
        l.append(root.val)
        if root.left!=None:
            l = self.preorder(root.left,l)
        if root.right!=None:
            l = self.preorder(root.right,l)
        return l
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        k = []
        return self.preorder(root,k)