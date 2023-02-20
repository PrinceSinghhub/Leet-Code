# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):

        if root is None: return
        if root.val == key:
            if root.right and root.left:
                right = root.right
                while right is not None and right.left is not None: right = right.left
                right.left = root.left
                return root.right
            else:
                if root.left:
                    return root.left
                elif root.right:
                    return root.right
                else:
                    return None

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root