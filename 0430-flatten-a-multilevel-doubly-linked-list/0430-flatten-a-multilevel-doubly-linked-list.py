"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        curr = head

        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                
                curr.next = curr.child
                curr.child.prev = curr

                
                curr.child = None


            if curr.next is None and stack:

                node = stack.pop()

                curr.next = node
                node.prev = curr

            
            curr = curr.next

        return head                    
