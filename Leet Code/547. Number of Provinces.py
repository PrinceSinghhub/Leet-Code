class Solution:
	def findCircleNum(self, isConnected):

		def find_connected_cities(row):
			for column in range(len(isConnected[0])):
				if isConnected[row][column] == 1 and self.visited[column] != True:
					self.visited[column] = True
					find_connected_cities(column)

		self.visited = [False] * len(isConnected)
		result = 0
		for row in range(len(isConnected)):
			if self.visited[row] != True:
				for column in range(len(isConnected[0])):
					if isConnected[row][column] == 1 and self.visited[column] !=  True:
						result += 1
						self.visited[row] = True
						find_connected_cities(row)
		return result

ans = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(ans.findCircleNum(isConnected))