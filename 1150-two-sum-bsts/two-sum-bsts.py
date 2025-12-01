# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs_and_add(self, node, n_set):
        if (node is None):
            return
        n_set.add(node.val)
        self.bfs_and_add(node.left, n_set)
        self.bfs_and_add(node.right, n_set)

    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        set_t1 = set()
        set_t2 = set()

        self.bfs_and_add(root1,set_t1)
        self.bfs_and_add(root2,set_t2)
        for k in set_t1:
            if target-k in set_t2:
                return True
        return False
