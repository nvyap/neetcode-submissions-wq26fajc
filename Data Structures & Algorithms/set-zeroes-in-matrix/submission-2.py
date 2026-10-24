class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False  # whether the first row itself must be zeroed

        # Pass 1: mark which rows/cols need zeroing using row 0 & col 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0          # mark column c
                    if r > 0:
                        matrix[r][0] = 0      # mark row r
                    else:
                        rowZero = True        # row 0 can't mark itself

        # Pass 2: zero the interior using the markers (skip row 0 / col 0)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Pass 3: apply markers to column 0 and row 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0