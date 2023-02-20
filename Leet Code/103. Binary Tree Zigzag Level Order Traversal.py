# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        level = 1
        res, curr, nxt = [], [root], []

        while curr:

            for i in curr:
                if i.left:
                    nxt.append(i.left)
                if i.right:
                    nxt.append(i.right)
            if level % 2 == 0:
                curr.reverse()
            res.append([i.val for i in curr])
            curr = nxt
            if nxt:
                level += 1
            nxt = []
        return res
