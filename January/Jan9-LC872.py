# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # can do dfs or bfs
        # lets do dfs. define new function inside to make array of leafs

        def getLeafs(root, leafArray):
            if root is None:
                return

            if root.left == None and root.right == None:
                leafArray.append(root.val)
                return leafArray
            
            getLeafs(root.left, leafArray)
            getLeafs(root.right, leafArray)

            return leafArray

        return getLeafs(root1,[]) == getLeafs(root2,[])


