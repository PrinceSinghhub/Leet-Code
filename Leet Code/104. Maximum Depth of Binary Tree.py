class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        Left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(Left, right) + 1


ans = Solution()
root = [3,9,20,'null','null',15,7]
print(ans.maxDepth(root))