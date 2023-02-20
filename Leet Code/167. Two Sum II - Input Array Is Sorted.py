class Solution:
    def twoSum(self, numbers, target):


        # ans = []
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #
        #         if numbers[i]+numbers[j] == target:
        #             ans.append(i+1)
        #             ans.append(j+1)
        #             break
        # return ans

    # apply binarySearch
         start = 0
         end = len(numbers)-1
        
         while start<end:
            Sum = numbers[start]+numbers[end]
            if Sum == target:
                return [start+1,end+1]
            elif Sum > target:
                end = end-1
            elif Sum < target:
                start = start+1



ans = Solution()
numbers = [-1,0]
target = -1
print(ans.twoSum(numbers,target))
