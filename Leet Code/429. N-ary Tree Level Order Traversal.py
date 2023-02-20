"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):

        if not root:
            return []

        ans = []
        level = [root]

        while level:
            ans.append([node.val for node in level])
            level = [kid for node in level for kid in node.children if kid != None]

        return ans