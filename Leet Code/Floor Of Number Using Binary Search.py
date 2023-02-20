class Solution:
    def FloorNumber(self,arr,element):
        start = 0
        end = len(arr) - 1

        if(element<arr[0]):
            return "Sorry No Floor Value Flound! "

        while (start <= end):
            mid = start + (end - start) // 2

            if (element > arr[mid]):
                start = mid + 1

            if (element < arr[mid]):
                end = mid - 1

            if (arr[mid] == element):
                return f"Celling Number of {element} is: {arr[mid]}"

        return f"Celling Number of {element} is: {arr[end]}"

r = Solution()
nums = [2,3,5,9,14,16,18]
n = 7
print(r.FloorNumber(nums,n))
