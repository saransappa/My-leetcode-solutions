# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root, l):
        if root==None:
            return l
        if root.left!=None:
            l = self.postorder(root.left,l)
        if root.right!=None:
            l = self.postorder(root.right,l)
        l.append(root.val)
        return l
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        k = []
        return self.postorder(root,k)