class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        res=[[0] * row for _ in range(col)]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                res[i][j]=matrix[j][i]

        

           
        return res
        