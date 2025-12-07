# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.val == None:
            return None
        if head.next == None:
            return head
        node = head
        l = []
        while(node != None):
            l.append(node.val)
            node = node.next
        l.sort()

        head = ListNode(l[0])
        node = head
        for i in range(1,len(l)):
            node.next = ListNode(l[i])
            node = node.next
        
        return head
        