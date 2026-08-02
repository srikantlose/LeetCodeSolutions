# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow=head,head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        while slow:
            nextRef=slow.next
            slow.next=prev
            prev=slow
            slow=nextRef
        
        L,R=head,prev
        while L and R:
            if(L.val!=R.val):
                return False
            L=L.next
            R=R.next
        return True