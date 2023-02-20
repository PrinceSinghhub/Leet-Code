class Solution:
    def reverseVowels(self, s):

        check = ['a', 'e', 'i', 'o', 'u']
        vol = ""

        for i in s:
            if i.lower() in check:
                vol += i

        ansarr = [(i if i.lower() not in check else '^') for i in s]
        print(ansarr)


        vol = vol[::-1]
        print(vol)


        temp = ''.join(ansarr)

        ans= ''
        index = 0
        for i in temp:
            if i == "^":
                ans+=vol[index]
                index+=1
            else:
                ans+=i
        return ans


ans = Solution()
s = "leetcode"
print(ans.reverseVowels(s))

