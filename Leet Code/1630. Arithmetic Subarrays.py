class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):

        answer = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i] + 1]
            temp.sort()
            x = temp[1] - temp[0]
            flag = 0
            for j in range(2, len(temp)):
                if temp[j] - temp[j - 1] != x:
                    flag = 1
                    break
            if flag == 0:
                answer.append(True)
            else:
                answer.append(False)
        return answer

ans = Solution()
nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]
print(ans.checkArithmeticSubarrays(nums,l,r))