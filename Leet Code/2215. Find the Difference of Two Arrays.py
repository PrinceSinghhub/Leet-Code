class Solution(object):
    def findDifference(self, nums1, nums2):
        # one line function
        # return [set(a) - set(b), set(b) - set(a)]

        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        temp = nums1.copy()

        for i in nums1:
            if i in nums2:
                temp.remove(i)
                nums2.remove(i)

        return [temp, nums2]

ans = Solution()
a=[-10,-5,-2,8,10,2]
b= [1,2,5,4,-10,-2,5]
print(ans.findDifference(a,b))