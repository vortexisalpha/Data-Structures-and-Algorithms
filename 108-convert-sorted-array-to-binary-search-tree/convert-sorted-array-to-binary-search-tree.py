# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def assign(self,arr):
        if (len(arr) == 0):
            return None
        mid = (len(arr)) //2
        cur = TreeNode(arr[mid],self.assign(arr[0:mid]),self.assign(arr[mid+1:len(arr)]))
        return cur

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.assign(nums)
        