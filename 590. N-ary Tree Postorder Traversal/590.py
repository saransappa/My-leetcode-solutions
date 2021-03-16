"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def po(self,root,l):
        if root==None:
            return l
        for i in root.children:
            if i != None:
                l = self.po(i,l)
        l.append(root.val)
        return l
    def postorder(self, root: 'Node') -> List[int]:
        k = []
        return self.po(root,k)