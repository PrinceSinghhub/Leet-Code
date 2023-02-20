# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        nextLevel = deque()
        vals = []
        
        while q:
            node = q.popleft()
            
            if node.left:
                nextLevel.append(node.left)
                vals.append(node.left.val)
            
            if node.right:
                nextLevel.append(node.right)
                vals.append(node.right.val)
                
            if len(q) == 0:
                if level % 2 == 0:
                    print(vals)
                    vals.reverse()
                    print(vals)
                    
                    for i in range(len(nextLevel)):
                        nextLevel[i].val = vals[i]
                    
                level += 1
                q = nextLevel
                nextLevel = deque()
                
        
        return root
        