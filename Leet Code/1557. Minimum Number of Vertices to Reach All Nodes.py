class Solution:
    def findSmallestSetOfVertices(self, n,edges):

        path = set(range(n))
        print(path)

        for key, val in edges:
            if val in path:
                path.remove(val)

        path = list(path)
        return path


n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
ans = Solution()
print(ans.findSmallestSetOfVertices(n,edges))