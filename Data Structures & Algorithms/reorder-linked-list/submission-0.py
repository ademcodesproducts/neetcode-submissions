class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next

        left, right = 0, len(values) - 1
        curr = head

        while left <= right:
            curr.val = values[left]
            left += 1
            curr = curr.next

            if left <= right:
                curr.val = values[right]
                right -= 1
                curr = curr.next