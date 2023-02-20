class Solution:
    def nextGreatestLetter(self, letters,target):


        if ord(target)==ord(letters[len(letters)-1]) or ord(target)>ord(letters[len(letters)-1]):
            return letters[0]

        for i in letters:
            if ord(i)>ord(target):
                return i

letters = ["c","f","j"]; target = "k"
r = Solution()
print(r.nextGreatestLetter(letters,target))
