# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):

        if head == None:
            return head

        if head.next == None:
            return head

        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head

        if not head.next.next or head.next.val != head.next.next.val:
            return self.deleteDuplicates(head.next.next)

        return self.deleteDuplicates(head.next)


