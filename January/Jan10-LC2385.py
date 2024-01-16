# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        # we know this is a binary tree. at most, only 3 nodes can get infected all at once. 
        # this is basically a height problem

        # if start is main root, return max(left, right) - 1
        
        # if start is not main root and not leaf node:::
        # it is height of the main subtree that the start node is in MINUS 2, plus height of other main subtree - 1

        # if start is a leaf node:::
        # it is height of left + right - 2

from typing import Optional


class Solution:

    def __init__(self):
        self.isLeaf=False
        self.leftHeight=0
        self.rightHeight=0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if root.val==start:
            return self.calculateHeight(root, start) - 1
        
        self.calculateHeight(root, start)
        if self.isLeaf:
            return self.leftHeight + self.rightHeight - 3
        else:
            return self.leftHeight + self.rightHeight - 2

    def calculateHeight(self,root, start):
        if root is None:
            return 0
        if root.val==start and root.left is None and root.right is None:
            isLeaf=True
            return 0

        self.leftHeight = self.calculateHeight(root.left, start)
        self.rightHeight = self.calculateHeight(root.right, start)

        return max(self.leftHeight, self.rightHeight) + 1
        





# class Solution:
#     def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
#         graph = defaultdict(list)
        
#         stack = [(root, None)]
#         while stack: 
#             n, p = stack.pop()
#             if p: 
#                 graph[p.val].append(n.val)
#                 graph[n.val].append(p.val)
#             if n.left: stack.append((n.left, n))
#             if n.right: stack.append((n.right, n))
        
#         ans = -1
#         seen = {start}
#         queue = deque([start])
#         while queue: 
#             for _ in range(len(queue)): 
#                 u = queue.popleft()
#                 for v in graph[u]: 
#                     if v not in seen: 
#                         seen.add(v)
#                         queue.append(v)
#             ans += 1
#         return ans 
        