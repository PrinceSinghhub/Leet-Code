class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        '''0 = type
        1 = color
        2 = name'''
        res = 0


        if ruleKey == "type":
            index = 0
            l = len(items)
            for i in range(l):
                if items[i][index] == ruleValue:
                    res+=1

        if ruleKey == "color":
            index = 1
            l = len(items)
            for i in range(l):
                if items[i][index] == ruleValue:
                    res+=1

        if ruleKey == "name":
            index = 2
            l = len(items)
            for i in range(l):
                if items[i][index] == ruleValue:
                    res+=1
        return res

List =  [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
n = "type"
m = "phone"
r = Solution()
print(r.countMatches(List,n,m))
