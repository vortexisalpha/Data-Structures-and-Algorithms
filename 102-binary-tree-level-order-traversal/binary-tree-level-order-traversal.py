# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return []
        def bfs(root):
            node_q = deque()
            node_q.append(root)
            
            while(len(node_q) > 0):
                lvl_list = []

                for i in range(len(node_q)):
                    node = node_q.popleft()
                    lvl_list.append(node.val)
                    if node.left is not None:
                        node_q.append(node.left)
                    if node.right is not None:
                        node_q.append(node.right)

                nonlocal ans
                ans.append(lvl_list)
        bfs(root)
        return ans
            