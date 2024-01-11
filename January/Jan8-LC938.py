# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mySum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # nice and easy. do a dfs 
        
        def dfs(root):
            if root == None:
                return

            dfs(root.left)
            dfs(root.right)
            if low <= root.val <= high:
                self.mySum+=root.val 

        dfs(root)
        return self.mySum    
    
