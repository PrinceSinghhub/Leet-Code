# https://leetcode.com/problems/maximum-population-year/
class Solution:
    def maximumPopulation(self, logs):
        lives = []

        for i in range(len(logs)):
            lives.append(1)

        L = len(logs)-1
        while L>=0:
            l = len(logs)-1
            while l >= 1:
                if logs[l][0] < logs[l - 1][1]:
                    lives[l]+=1

                l-=1






        return lives

ans = Solution()
arr = [[1950,1961],[1960,1971],[1970,1981]]
print(ans.maximumPopulation(arr))

