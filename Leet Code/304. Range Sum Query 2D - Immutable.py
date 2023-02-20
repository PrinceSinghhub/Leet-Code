class NumMatrix:

    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        self.range_sum = [[0] * cols for _ in range(rows)]
        self.range_sum[0][0] = matrix[0][0]
        for col in range(1, cols):
            self.range_sum[0][col] = self.range_sum[0][col - 1] + matrix[0][col]

        for row in range(1, rows):
            self.range_sum[row][0] = self.range_sum[row - 1][0] + matrix[row][0]

        for row in range(1, rows):
            for col in range(1, cols):
                self.range_sum[row][col] = matrix[row][col] + self.range_sum[row - 1][col] + self.range_sum[row][
                    col - 1] - self.range_sum[row - 1][col - 1]

    def sumRegion(self, row1, col1, row2, col2):
        if row1 == 0 and col1 == 0:
            return self.range_sum[row2][col2]
        if row1 == 0:
            return self.range_sum[row2][col2] - self.range_sum[row2][col1 - 1]
        if col1 == 0:
            return self.range_sum[row2][col2] - self.range_sum[row1 - 1][col2]

        return self.range_sum[row2][col2] - self.range_sum[row1 - 1][col2] - self.range_sum[row2][col1 - 1] + \
               self.range_sum[row1 - 1][col1 - 1]


