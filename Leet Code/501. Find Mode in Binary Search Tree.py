# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def Val(self, root, mydic):

        # mydic = {}

        if root is None:
            return mydic

        if root.val in mydic:
            mydic[root.val] += 1

        if root.val not in mydic:
            mydic[root.val] = 1

        if root.left != None:
            self.Val(root.left, mydic)

        if root.right != None:
            self.Val(root.right, mydic)

        return mydic

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        ans = self.Val(root, {})

        Max = max(ans.values())

        arr = []

        for key, val in ans.items():

            if Max == val:
                arr.append(key)

        return arr









