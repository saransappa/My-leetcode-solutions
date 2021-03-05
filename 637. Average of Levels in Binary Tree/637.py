# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,k,l):
        if root.left!=None:
            self.inorder(root.left,k+1,l)
        
        p = []
        p.append(root.val)
        p.append(k)
        l.append(p)
        if root.right!=None:
            self.inorder(root.right,k+1,l)
        return l
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        l = []
        l = self.inorder(root,0,l)
        
        d = {}
        c = {}
        for i in l:
            if d.get(i[1],'!')=='!':
                d[i[1]] = i[0]
                c[i[1]] = 1
            else:
                d[i[1]]+=i[0]
                c[i[1]]+=1
        ans = []
        max_depth = -1
        for i in d.keys():
            max_depth = max(max_depth,i)
            
        for i in range(max_depth+1):
            r = d[i]/c[i]
            ans.append(r)
        return ans