class Solution:
    def rotate(self, nums,k):

        last = nums[:len(nums)-k]
        first = []

        for i in range(k,0,-1):
            first.append(nums[-i])

        output = []

        for k in first:
            output.append(k)

        for j in last:
            output.append(j)

        # nums[:] = output for leet code

        return output
        # print(last)
        # print(first)



k=2
a=[-1,-100,3,99]
r = Solution()
print(r.rotate(a,k))
# r.rotate(a,k)