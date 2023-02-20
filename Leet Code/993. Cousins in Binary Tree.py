# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        treeDict = {}
        tree = [] # See optimization note below
        tree.append((root, 0, 0))
        while tree:
            node, parent, depth = tree.pop(0)
            if node is not None:
                treeDict[node.val] = (parent, depth) # See optimization note below
                tree.append((node.left, node.val, depth+1))
                tree.append((node.right, node.val, depth+1))
        return treeDict[x][1] == treeDict[y][1] and treeDict[x][0] != treeDict[y][0]
        