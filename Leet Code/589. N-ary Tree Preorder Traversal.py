"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
            if not root:
                return []
            children = []
            for node in root.children:
                children += self.preorder(node)
            return [root.val] + children


ans = Solution()
root = [1,null,3,2,4,null,5,6]
print(ans.preorder(root))
