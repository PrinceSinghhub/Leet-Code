class Solution:
    def reverseWords(self, s):

        # words = s.split()
        # output = " ".join(word[::-1] for word in words)
        s = s.strip()

        List = []
        a = ""
        for i in s:
            if i == " ":
                List.append(a)
                a = ""
            else:
                a+=i
        List.append(a)
        ans = ""
        for i in List:
            rev = i[::-1]
            ans+=rev+" "
        return ans.strip()



ans = Solution()
s = "Let's take LeetCode contest"
print(ans.reverseWords(s))

