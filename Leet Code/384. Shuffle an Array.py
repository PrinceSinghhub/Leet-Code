class Solution:

    def __init__(self, nums: List[int]):
        self.a = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return list(self.a)

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        x = list(self.a)
        ans = []
        while x:
            i = random.randint(0, len(x) - 1)
            x[i], x[-1] = x[-1], x[i]
            ans.append(x.pop())
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

arr = [[[1, 2, 3]], [], [], []]
ans = Solution(arr)
a = ["Solution", "shuffle", "reset", "shuffle"]
print(ans.reset())
