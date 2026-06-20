# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        llSet = set()
        node = head

        while node:
            if node in llSet:
                return True
            else:
                llSet.add(node)
            node = node.next
        return False            










        # slow = fast = head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False        








        