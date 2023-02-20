# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        if root == None:
            return []
        result= [ str(root.val)+"->" + path for path in self.binaryTreePaths(root.left)]
        result+= [ str(root.val)+"->" + path for path in self.binaryTreePaths(root.right)]
        return result or [str(root.val)]  # if empty return leaf itself