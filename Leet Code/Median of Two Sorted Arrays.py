class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        nums1 = nums1 + nums2
        nums1len = len(nums1)
        halflen = nums1len // 2
        nums1.sort()
        if (nums1len % 2 != 0):
            return nums1[halflen]
        else:
            return (nums1[halflen - 1] + nums1[halflen]) / 2


ans = Solution()
nums1 = [1,3]
nums2 = [2]
print(ans.findMedianSortedArrays(nums1,nums2))