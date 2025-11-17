# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node is None:
            return
        self.cnt+=1
        self.dfs(node.left)
        self.dfs(node.right)
        
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        self.dfs(root)
        return self.cnt