# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totalNode = 0
        node = dummy = head
        while node:
            totalNode += 1
            node = node.next
        deleteNode = totalNode - n
        if deleteNode == 0:
            return head.next
        cnt = 1
        while dummy:
            if cnt == deleteNode:
                dummy.next = dummy.next.next
            dummy = dummy.next
            cnt+=1       
        return head    
        