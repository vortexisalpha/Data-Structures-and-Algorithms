# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.ptr = -1
        self.node = root
        self.seen = set()
        self.parent_map = {}
        while(self.node.left != None):
            self.parent_map[self.node.left] = self.node
            self.node = self.node.left


    def next(self) -> int:
        if self.ptr == -1:
            self.ptr = self.node.val
            self.seen.add(self.ptr)
            return self.ptr

        if self.node.right != None and self.node.right.val not in self.seen:
            self.parent_map[self.node.right] = self.node
            self.node = self.node.right 
            while(self.node.left != None):
                self.parent_map[self.node.left] = self.node
                self.node = self.node.left
            self.ptr = self.node.val
            self.seen.add(self.ptr)
            return self.ptr
        else:
            while(self.node.val in self.seen):
                self.node = self.parent_map[self.node]
            self.ptr = self.node.val
            self.seen.add(self.ptr)
            return self.ptr
            

    def hasNext(self) -> bool:
        if self.node.right != None:
            return True
        temp = self.node
        while(temp.val in self.seen):
            if temp in self.parent_map:
                temp = self.parent_map[temp]
            else: 
                break
        if temp.val not in self.seen:
            return True
        return False
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()