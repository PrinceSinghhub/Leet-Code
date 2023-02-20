class Solution:
    def isBalanced(self, root):

        self.answer = True

        def validate_tree(root):
            if not root:
                return 0
            left = validate_tree(root.left)
            right = validate_tree(root.right)

            if abs(left - right) > 1:
                self.answer = False
            return 1 + max(left, right)

        validate_tree(root)
        return self.answer

ans = Solution()
root = [3,9,20,null,null,15,7]
print(ans.answer(root))