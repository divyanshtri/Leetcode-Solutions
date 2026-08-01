class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j>i:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for  k in range(len(matrix)):
            matrix[k].reverse()
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        