# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        list_elems = []
        curr = head
        while curr:
            list_elems.append(curr.val)
            curr = curr.next

        list_elems.reverse()

        curr = head
        for val in list_elems:
            curr.val = val
            curr = curr.next
        
        return head

            
