# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur=head
        dummy=ListNode(0)
        tail=dummy
        check=set()
        while cur:
            tail.next=cur
            if tail.next in check:
                return True
            else:
                check.add(cur)
            cur=cur.next
        tail.next 
        return False
        