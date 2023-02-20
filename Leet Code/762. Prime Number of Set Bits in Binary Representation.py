class Solution(object):
    def findprime(self, num):

        count = 2
        while count * count <= num:
            if num % count == 0:
                return False

            count += 1

        return True

    def countPrimeSetBits(self, left, right):

        nbit = []

        for i in range(left, right + 1):
            ans = bin(i).count('1')

            nbit.append(ans)

        count = 0

        for i in nbit:
            if i >= 2:
                ans = self.findprime(i)
                if ans == True:
                    count += 1

        return count



ans = Solution()
left = 6
right = 10
print(ans.countPrimeSetBits(left,right))