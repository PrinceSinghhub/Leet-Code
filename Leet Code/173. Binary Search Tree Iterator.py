# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
            self.btree = []
            self.index = -1
            self.inorder(root)

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.btree.append(node.val)
        self.inorder(node.right)

    def next(self) -> int:
        self.index+=1
        return self.btree[self.index]


    def hasNext(self) -> bool:
        if self.index +1 < len(self.btree):
            return True
        return False
