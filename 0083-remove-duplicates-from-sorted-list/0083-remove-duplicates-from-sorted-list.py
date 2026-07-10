# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        ptr=head
        while curr:
            if curr.next==None:
                ptr.next=curr.next
                curr=None
            elif curr.next.val==curr.val:
                curr=curr.next
            else:
                ptr.next=curr.next
                curr=curr.next
                ptr=curr
        return head
            
        