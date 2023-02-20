class Solution:
    def removeStars(self, s: str) -> str:
        
        
        stack = []
        
        for i in s:
            if i != '*':
                stack.append(i)
            else:
                stack.pop()
        
        
        print(stack)
        
        
        if len(stack) == 0:
            return ""
        ans = ""
        for i in stack:
            ans+=i
        return ans