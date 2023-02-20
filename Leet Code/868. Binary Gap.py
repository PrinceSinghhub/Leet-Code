class Solution:
    def binaryGap(self, n):

        arr = []

        Bin = bin(n)[2::]
        print(Bin)

        count = 0
        for i in Bin:

            if i == '1':
                arr.append(count)

            count += 1

        arr.sort()
        print(arr)
        ans = []
        for i in range(len(arr) - 1, -1, -1):

            if i == 0:
                break
            count = arr[i] - arr[i - 1]

            ans.append(count)

        print(ans)
        if len(ans) == 0:
            return 0
        return max(ans)


ans = Solution()
n = 22
print(ans.binaryGap(n))