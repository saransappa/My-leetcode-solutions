# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.z = set()
    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        self.z.add(root.val)
        if root.right!=None:
            self.inorder(root.right)
        
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.inorder(root)
        k = list(self.z)
        k.sort()
        if len(k)>=2:
            return k[1]
        else:
            return -1