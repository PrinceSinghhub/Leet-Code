class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {letter:index for index,letter in enumerate(S)}
        outlist = []
        count = 0
        pos = 0
        for index,letter in enumerate(S):
            count += 1
            pos = max(pos,d[letter])
            if index == pos:
                outlist.append(count)
                count = 0
        return outlist


ans = Solution()
s = "ababcbacadefegdehijhklij"
print(ans.partitionLabels(s))
