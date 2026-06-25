# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        slow = curr
        fast = curr
        stack = []

        # Store first half in stack
        while fast and fast.next :
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            curr1 = slow.next
        else:
            curr1 = slow

        while curr1:

            if not stack:
                return False

            if curr1.val == stack[-1]:
                stack.pop()
                curr1 = curr1.next
            else:
                return False

    
        return len(stack) == 0
        