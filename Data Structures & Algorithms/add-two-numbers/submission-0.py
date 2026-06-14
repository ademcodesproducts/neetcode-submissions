# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            value = total % 10
            carry = total // 10

            curr.next = ListNode(value)

            if not l1 and not l2 and carry != 0:
                curr.next = ListNode(carry)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            curr = curr.next

        return dummy.next
        