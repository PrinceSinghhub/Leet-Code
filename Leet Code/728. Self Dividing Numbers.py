class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []

        for num in range(left, right + 1):
            if num < 10:
                res.append(num)
            else:
                temp = num
                while temp != 0:
                    div = temp % 10
                    if div != 0 and num % div == 0:
                        temp //= 10
                    else:
                        break
                if temp == 0:
                    res.append(num)
        return res


ans = Solution()
left = 1
right = 22
print(ans.selfDividingNumbers(left,right))