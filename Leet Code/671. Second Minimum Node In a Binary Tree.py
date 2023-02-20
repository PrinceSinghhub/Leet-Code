# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def InOrder(self, root):

        if root == None:
            return []

        left = self.InOrder(root.left)
        right = self.InOrder(root.right)

        return left + [root.val] + right

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        arr = self.InOrder(root)

        arr = list(set(arr))
        arr.sort()

        if len(arr) < 2:
            return -1

        return arr[1]



