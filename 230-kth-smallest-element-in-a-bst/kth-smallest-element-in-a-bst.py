# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def bfs(self, node):
        if node is None:
            return
        self.vals.append(node.val)
        self.bfs(node.left)
        self.bfs(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.vals = []
        self.bfs(root)
        self.vals = sorted(self.vals)
        return self.vals[k-1]
        
        