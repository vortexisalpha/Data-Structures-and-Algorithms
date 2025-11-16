class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        [1 4 7]
        [6 5 4]
        [9 8 7]
        
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                
                a = matrix[j][i]
                b = matrix[i][j]
                matrix[i][j] = a
                matrix[j][i] = b

        print(matrix)
        for i in range(n):
            matrix[i].reverse()
            
