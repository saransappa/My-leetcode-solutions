# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return root
        nodes  = []
        def inorder(temp):
            if temp.left!=None:
                inorder(temp.left)
            nodes.append(temp)
            if temp.right!=None:
                inorder(temp.right)
        inorder(root)
        for i in nodes:
            i.left,i.right = i.right,i.left
            
        return root