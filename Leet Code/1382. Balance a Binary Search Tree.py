# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bst(self, nums, i, j):
        if i > j:
            return None
        mid = (i+j) // 2
        node = TreeNode(nums[mid])
        node.left = self.bst(nums, i, mid-1)
        node.right = self.bst(nums, mid+1, j)
        return node
    
    def dfs(self, node):
        if not node:
            return []
        l, r = self.dfs(node.left), self.dfs(node.right)
        return l + [node.val] + r
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.dfs(root)
        return self.bst(nums, 0, len(nums)-1)
    
# ansother approch
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        nums = []
        
        def inorder( node,nums):
            '''
            Convert BST to ascending sequence
            '''    
            if node:
                
                inorder( node.left, nums )
                nums.append( node.val )
                inorder( node.right, nums )
                
        # ----------------------------------------
        
        def sequence_to_balanced_BST( left, right, nums):
            '''
            Convert ascending sequence to balanced BST
            '''
            if left > right:
                # Base case:
                return None
            
            else:
                # General case:

                mid = left + ( right - left ) // 2

                root = TreeNode( nums[mid] )

                root.left = sequence_to_balanced_BST( left, mid-1, nums)
                root.right = sequence_to_balanced_BST( mid+1, right, nums)

                return root
        
        # ----------------------------------------
		
        # Flatten original BST into a ascending sorted sequence.
        inorder( root, nums )
        
		# Convert asecnding sorted sequence into Balanced BST by the algorithm in Leetcode #108
        return sequence_to_balanced_BST( left = 0, right = len(nums)-1, nums = nums)