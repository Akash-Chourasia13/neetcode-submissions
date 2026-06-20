# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        height = self.depth(root,height)
        return height

    def depth(self,root,height):
        if root==None:
            return height
        height+=1
        height = max(self.depth(root.left,height),self.depth(root.right,height))
        return height        
        