# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr=head
        slow=curr
        fast=curr

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next 

        curr1=slow.next
        slow.next=None
        prev=None

        while curr1!=None:
            new_node=curr1.next
            curr1.next=prev
            prev=curr1
            curr1=new_node

        while curr!=None and prev!=None:
            temp1=curr.next
            temp2=prev.next

            curr.next=prev
            prev.next=temp1

            curr = temp1
            prev = temp2
            

