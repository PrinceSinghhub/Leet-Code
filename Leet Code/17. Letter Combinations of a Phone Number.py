class Solution:
    def letterCombinations(self, digits):

        if len(digits) == 0:
            return []

        hashmap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        result = []

        if len(digits) == 0:
            return []

        def backtrack(index, path):
            if len(digits) == len(path):
                result.append("".join(path))
                return

            letters = hashmap[digits[index]]

            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result


ans = Solution()
digits = "23"
print(ans.letterCombinations(digits))
