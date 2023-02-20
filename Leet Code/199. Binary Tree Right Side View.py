# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []
        ans = [root.val]
        left = ans + self.rightSideView(root.left)
        right = ans + self.rightSideView(root.right)
        if len(right) >= len(left):
            return right
        return right + left[len(right):]
