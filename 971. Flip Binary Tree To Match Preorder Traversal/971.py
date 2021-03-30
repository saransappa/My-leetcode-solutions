# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        z = []
        z = self.preorder(root,z)
        print(z)
        ans = []
        i = 0
        while i < len(voyage):
            if z[i]==None:
                print("EOF z")
                break
            if voyage[i]==None:
                print("EOF voyage")
                break
                
            if z[i]==voyage[i]:
                i+=1
            else:
                if i>=1:
                    if voyage[i-1] not in ans:
                        self.flip(root,voyage[i-1])
                        ans.append(voyage[i-1])
                    else:
                        return [-1]
                    print(ans)
                    p = []
                    z = self.preorder(root,p)
                else:
                    return [-1]
        return ans       
            
    def flip(self,root,k):
        if root==None:
            return
        if root.val==k:
            p = root.left
            root.left = root.right
            root.right = p
            return
        else:
            if root.left!=None:
                self.flip(root.left,k)
            if root.right!=None:
                self.flip(root.right,k)

    def preorder(self,root,z):
        if root==None:
            return z
        z.append(root.val)
        if root.left!=None:
            z = self.preorder(root.left,z)
        if root.right!=None:
            z = self.preorder(root.right,z)
        return z
        
        