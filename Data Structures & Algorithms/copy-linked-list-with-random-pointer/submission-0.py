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
        copy_map = {}

        curr = head
        while curr:
            copy = Node(curr.val, None, None)
            copy_map[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = copy_map[curr]
            copy.next = copy_map.get(curr.next)
            copy.random = copy_map.get(curr.random)
            curr = curr.next

        return copy_map[head] if head else None