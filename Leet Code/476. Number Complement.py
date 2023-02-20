class Solution:
    def findComplement(self, num):

        convert = bin(num)[2::]
        print(convert)

        comp = ""
        for i in convert:
            if i == '0':
                comp += '1'

            elif i == '1':
                comp += '0'

        print(comp)
        ans = int(comp, 2)
        return ans

        # optimize code

    # return num ^ (2 ** num.bit_length() - 1)


ans = Solution()
num = 1254899254
print(ans.findComplement(num))