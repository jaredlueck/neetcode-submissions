class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = [(9 * [False]) for i in range(9)]
        col_map = [(9 * [False]) for i in range(9)]
        
        grid_map = [(9 * [False]) for i in range(9)]
        
        for row in range(9):
            for col in range(9):
                grid_number = 3 * (row // 3) + (col // 3)
                if board[row][col] != ".":
                    val = int(board[row][col])
                    
                    # Check if the current row, column or box contains the current value already
                    if row_map[row][val-1]:
                        return False
                    if col_map[col][val-1]:
                        return False
                    if grid_map[grid_number][val-1]:
                        return False
                    
                    row_map[row][val-1] = True
                    col_map[col][val-1] = True
                    grid_map[grid_number][val-1] = True

        return True


                
