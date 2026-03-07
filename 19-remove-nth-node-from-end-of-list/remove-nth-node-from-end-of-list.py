# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0 
        it = head
        while it != None:
            it = it.next
            count+=1

        it = head
        print(count)
        if count - n - 1 < 0:
            return head.next
        for i in range(count-n-1):
            it = it.next

        if it.next is not None and it.next.next is not None:
            it.next = it.next.next
        else:
            it.next = None
        return head

