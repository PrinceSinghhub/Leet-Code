# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        # recursive solution
        answer = 0
        if root == None:
            return 0

        if root.left != None:
            if root.left.left == None and root.left.right == None:
                answer += root.left.val
            else:
                answer += self.sumOfLeftLeaves(root.left)

        answer += self.sumOfLeftLeaves(root.right)
        return answer


ans = Solution()
root = [3,9,20,'null','nul',15,7]
print(ans.sumOfLeftLeaves(root))