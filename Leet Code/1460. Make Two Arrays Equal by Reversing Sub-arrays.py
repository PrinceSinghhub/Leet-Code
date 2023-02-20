class Solution:
    def canBeEqual(self, target,arr):

        for i in arr:
            if i in target and arr.count(i) == target.count(i):
                continue
            else:
                return False

        return True


ans = Solution()
target = [1,2,3,4]
arr = [2,4,1,3]
print(ans.canBeEqual(target,arr))


