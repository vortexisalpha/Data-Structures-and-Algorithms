# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node,sum):
        sum += node.val
        if (node.left == None and node.right == None and sum == self.targetSum): self.flag = True
        if node.left != None: self.dfs(node.left, sum)
        if node.right != None: self.dfs(node.right, sum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        self.targetSum = targetSum
        self.flag = False
        self.dfs(root,0)
        return self.flag