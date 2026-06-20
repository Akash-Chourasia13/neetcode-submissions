# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = dummy = node = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow.next 
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        dummy2 = prev
        
        # 2->4->6   8
        while node and dummy2:
            fut1 = node.next
            fut2 = dummy2.next
            node.next = dummy2
            node = fut1
            dummy2.next = node
            dummy2 = fut2
        return None    





        