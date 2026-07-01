# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxDepth = 0
        return self.depth(root,maxDepth)

    def depth(self,root,maxDepth):
        if root is None:
            return maxDepth

        maxDepth = max(self.depth(root.left,maxDepth + 1),self.depth(root.right,maxDepth+1))
        return maxDepth        
        