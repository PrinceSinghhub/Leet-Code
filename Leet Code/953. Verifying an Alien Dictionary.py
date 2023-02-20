class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if words == None:
            return -1
        if order == None:
            return -1
        l,r = 0,1
        while len(words)>1:
            for i in range(len(words[l])):
                i_c = order.index(words[l][i])
                if i < len(words[r]):
                    r_c = order.index(words[r][i])
                    if i_c < r_c:
                        break
                    elif i_c == r_c:
                        continue
                    else:
                        return False
                else:
                    return False
            words.pop(l)
        return True


ans = Solution()
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(ans.isAlienSorted(words,order))