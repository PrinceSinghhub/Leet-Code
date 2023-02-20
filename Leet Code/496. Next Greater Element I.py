class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                x = stack.pop()
                d[x] = i
            stack.append(i)

        for i in range(len(nums1)):
            if nums1[i] in d:
                nums1[i] = d[nums1[i]]
            else:
                nums1[i] = -1
        return nums1

ans= Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(ans.nextGreaterElement(num1,nums2))