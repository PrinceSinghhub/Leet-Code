class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        children = [[] for i in range(n)]
        for i, m in enumerate(manager):
            if m >= 0: children[m].append(i)

        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        return dfs(headID)

