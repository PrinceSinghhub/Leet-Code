from collections import Counter
class Solution:
    def topKFrequent(self, nums,k):

        arr = Counter(nums)

        print(arr)

        frequest = []

        for key, val in arr.items():
            frequest.append(val)

        frequest.sort()
        frequest = frequest[::-1]

        print(frequest)

        ans = []

        for i in range(k):

            for key, val in arr.items():

                if frequest[i] == val and key not in ans:
                    ans.append(key)

        return ans

ans = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(ans.topKFrequent(nums,k))




