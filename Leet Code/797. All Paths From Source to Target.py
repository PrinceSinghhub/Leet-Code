class Solution:

    def explore(self, graph, res, node, path):
        if node == len(graph) - 1:    return path + [node]

        for neighbour in graph[node]:
            new_path = self.explore(graph, res, neighbour, path + [node])
            if new_path:
                res.append(new_path)

        return False

    def allPathsSourceTarget(self, edges):

        graph = {i: x for i, x in enumerate(edges)}

        res = []
        self.explore(graph, res, 0, [])

        return res

ans = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(ans.allPathsSourceTarget(graph))