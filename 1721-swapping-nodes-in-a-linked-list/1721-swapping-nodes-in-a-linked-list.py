# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        leng=head
        while leng:
            length+=1
            leng=leng.next 
        
        dummy=ListNode(0)
        dummy.next=head
        curr1=dummy
        for i  in range (k):
            curr1=curr1.next
        curr2=dummy
        for j in range (length-k+1):
            curr2=curr2.next
            
        curr1.val, curr2.val = curr2.val, curr1.val

        return dummy.next
        