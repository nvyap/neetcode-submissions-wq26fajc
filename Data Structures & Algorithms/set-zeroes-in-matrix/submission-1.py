class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols = len(matrix),len(matrix[0])
        r = 0
        c = 0
        hm = set()
        while r<rows:
            while c<cols:
                if matrix[r][c]==0:
                    hm.add((r,c))
                c += 1
            r += 1
            c = 0
        
        for i in hm:
            r1,c1 = i[0],i[1]
            for k in range(rows):
                matrix[k][c1] = 0
            for j in range(cols):
                matrix[r1][j] = 0

            