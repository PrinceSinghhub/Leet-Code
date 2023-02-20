class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = [jewels.count(i) for i in stones]
        return sum(ans)


ans = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(ans.numJewelsInStones(jewels,stones))