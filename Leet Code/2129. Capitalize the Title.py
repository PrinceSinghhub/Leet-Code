class Solution:

    def capitalizeTitle(self, title):
        title = title.split()
        print(title)

        ans = ""
        for i in title:
            print(i)

            if len(i) <= 2:
                ans += i.lower() + " "

            else:
                ans += i.title() + " "

        return ans.strip()

ans = Solution()
title = "First leTTeR of EACH Word"
print(ans.capitalizeTitle(title))