class Solution(object):
    def maximum69Number(self, num):

        ans = list(str(num))
        print(ans)

        for i in range(len(ans)):
            if ans[i] == '6':
                ans[i] = '9'
                break

        anss = ""
        for i in ans:
            anss += i
        return int(anss)

ans  = Solution()
nums = 9966
print(ans.maximum69Number(nums))