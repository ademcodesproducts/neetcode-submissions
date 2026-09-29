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

        og_copy_map = {}

        curr = head
        while curr:
            og_copy_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = og_copy_map[curr]
            copy.next = og_copy_map.get(curr.next)
            copy.random = og_copy_map.get(curr.random)
            curr = curr.next

        return og_copy_map.get(head)