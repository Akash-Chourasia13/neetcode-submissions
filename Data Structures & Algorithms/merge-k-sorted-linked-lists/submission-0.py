# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0 or not lists[0]:
            return None
        mergedList = lists[0]
        for i in range(1,len(lists)):
            mergedList = self.merge(mergedList,lists[i])
        return mergedList

    def merge(self,B,A):
        C = node = ListNode()
        while B and A:
            if B.val<=A.val:
                C.next = B
                B = B.next
            else:
                C.next = A
                A = A.next
            C = C.next   
        C.next = A or B
        return node.next               
        