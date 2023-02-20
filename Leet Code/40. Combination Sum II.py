class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))
        return (list, table[target])

ans = Solution()
candidates = [2,5,2,1,2]
target = 5
print(ans.combinationSum2(candidates,target))
