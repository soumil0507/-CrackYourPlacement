from typing import List


class Solution:
    def set_zero(self, matrix, m, n, row, col):

        # set row zero
        for i in range(n):
            matrix[row][i] = 0
        
        # set column zero
        for i in range(m):
            matrix[i][col] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        index_list = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    index_list.append([i, j])
        
        for index in index_list:
            self.set_zero(matrix, m, n, index[0], index[1])