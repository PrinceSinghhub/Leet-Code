# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)

        fast = slow = prev_of_slow = head
        # looking for median of list
        while fast and fast.next:
            prev_of_slow, slow, fast = slow, slow.next, fast.next.next

        # median = slow.val
        prev_of_slow.next = None
        return TreeNode(slow.val, left=self.sortedListToBST(head), right=self.sortedListToBST(slow.next))
