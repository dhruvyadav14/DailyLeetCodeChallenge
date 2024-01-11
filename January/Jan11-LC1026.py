# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        # lets do a dfs
        # keep track of the current min and max going down the subtree
        # the ways to obtain largest possible difference is node.val - minInSubtree or maxInSubtree - node.val
        def dfs(root):
            if root is None:
                return inf, -inf
            
            leftmin, leftmax=dfs(root.left)
            rightmin, rightmax=dfs(root.right)
            currmin, currmax=min(leftmin, rightmin, root.val), max(leftmax, rightmax, root.val)
            self.ans=max(root.val-currmin, currmax-root.val, self.ans)
            return currmin, currmax
        dfs(root)
        return self.ans