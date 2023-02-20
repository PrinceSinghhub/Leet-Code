class Solution:
    def nextGreatestLetter(self, letters,target):

        start = 0
        end = len(letters)-1

        if target==letters[end] or target>letters[end]:
            return letters[0]

        while(start<=end):

            mid = start+(end-start)//2

            if(target>=letters[mid]):
                start = mid+1

            if (target < letters[mid]):
                end = mid - 1

        return letters[start]
ans = Solution()
letters = ["c","f","j"]
target = "a"
print(ans.nextGreatestLetter(letters,target))
