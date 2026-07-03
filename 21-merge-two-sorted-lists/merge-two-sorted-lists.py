class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=list1
        head2=list2
        #list3=[]
        dummy = ListNode(0)
        tail = dummy
        cur1=head1
        cur2=head2
        while cur1 and cur2:
            if(cur1.val<cur2.val or cur1.val==cur2.val):
                tail.next=cur1
                cur1=cur1.next
            else:
                tail.next=cur2
                cur2=cur2.next
            tail = tail.next
        tail.next = cur1 or cur2
        return dummy.next