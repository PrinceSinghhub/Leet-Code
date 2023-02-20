class Solution:
    def sortSentence(self, s):

        mydic = {}

        indValue = ""
        for i in s:

            if i.isalpha():
                indValue += i

            if i.isdigit():
                mydic[int(i)] = indValue
                indValue = ""

        # sorted(mydic)
        #
        # ans = ""
        # for index, value in mydic.items():
        #     ans += value + " "
        #
        #
        # return ans.strip()
        ans = ""
        for i in range(1,len(mydic)+1):
            for index, value in mydic.items():
                if index == i:
                    ans+=value+" "
        return ans.strip()


ans = Solution()
s = "is2 sentence4 This1 a3"
print(ans.sortSentence(s))