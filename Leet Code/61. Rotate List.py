# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def onestep(head):
            temp = head
            while temp.next.next != None:
                temp = temp.next
            node = temp.next
            temp.next = None
            node.next = head
            return node

        def getlen(head):
            i = 0
            temp = head
            while temp:
                temp = temp.next
                i = i + 1
            return i

        if head == None or head.next == None:
            return head
        x = getlen(head)
        k = k % x
        for i in range(k):
            head = onestep(head)
        return head
