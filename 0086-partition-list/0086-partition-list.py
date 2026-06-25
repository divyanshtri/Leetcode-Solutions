# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1=ListNode(0)
        tail_s=dummy1
        dummy2=ListNode(00)
        tail_b=dummy2
        curr=head

        while curr!=None:
            if curr.val<x:
                tail_s.next=curr
                tail_s=tail_s.next
                curr=curr.next
            else:
                tail_b.next=curr
                tail_b=tail_b.next
                curr=curr.next
        tail_b.next=None
        tail_s.next=dummy2.next

        return dummy1.next