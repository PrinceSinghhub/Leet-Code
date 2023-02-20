class Solution:
    def intersect(self, nums1, nums2):

        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans
ans = Solution()
nums1=[1,2,2,1]
nums2 = [2,2]
print(ans.intersect(nums1,nums2))

