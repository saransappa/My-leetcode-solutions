# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self,root,d):
        if root.left!=None and root.right!=None:
            d = max(self.depth(root.left,d+1),self.depth(root.right,d+1))
        elif root.right!=None:
            d = self.depth(root.right,d+1)
        elif root.left!=None:
            d = self.depth(root.left,d+1)
        return d
    def depth2(self,root,d,k,sum):
        if d==k:
            sum+=root.val
        if root.left!=None and root.right!=None:
            x = self.depth2(root.left,d+1,k,0)
            y = self.depth2(root.right,d+1,k,0)
            d = max(x[0],y[0])
            sum = sum + x[1]+y[1];
        elif root.right!=None:
            x = self.depth2(root.right,d+1,k,0)
            d = x[0]
            sum+=x[1]
        elif root.left!=None:
            x = self.depth2(root.left,d+1,k,0)
            d = x[0]
            sum+=x[1]
        return (d,sum)
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        k = self.depth(root,0)
        p = self.depth2(root,0,k,0)
        return p[1]