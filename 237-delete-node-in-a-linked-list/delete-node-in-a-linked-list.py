# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr=node
        prev=None
        while curr.next and curr.next.next:
            nextVal=(curr.next).val
            curr.val=nextVal
            
            curr=curr.next
        nextVal=(curr.next).val
        curr.val=nextVal
        curr.next=None
       
        