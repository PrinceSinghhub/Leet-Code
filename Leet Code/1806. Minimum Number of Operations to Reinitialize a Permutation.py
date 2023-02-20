class Solution:
    def reinitializePermutation(self, n):

        perm = [i for i in range(n)]
        op = list(perm)
        arr = [0] * n
        c = 0
        nn = n // 2

        while arr != op:
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[int(nn + (i - 1) // 2)]
            perm = list(arr)

            c += 1
        return c

ans = Solution()
n = 2
print(ans.reinitializePermutation(n))