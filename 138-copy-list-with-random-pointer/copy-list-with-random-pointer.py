"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None


        top = head
        replacement = Node(top.val, None, top.random)
        l_m = {top : replacement, None : None}
        btm = top.next
        top = replacement

        while(btm is not None):
            replacement = Node(btm.val, None, btm.random)
            l_m[btm] = replacement
            top.next = replacement
            top = replacement
            btm = btm.next
        
        new_head = l_m[head]
        trav = new_head
        while(trav is not None):
            print("x")
            trav.random = l_m[trav.random]
            trav = trav.next

        return new_head