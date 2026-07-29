
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row check column check square, traverse 2d array row column
        #put a set at each checking criteria, out checking criteria are three groups
        #in each row, in each column, in each square so one set per that hence the placement of exist = set()
        for row in range(9):
            exist = set()
            for i in range (9):
                if board[row][i] == ".":
                    continue
                elif board[row][i] in exist:
                    return False
                else:
                    exist.add(board[row][i])
        for col in range(9):
            exist = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                elif board[i][col] in exist:
                    return False
                else:
                    exist.add(board[i][col])
        for square in range(9):
            exist = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) *3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in exist:
                        return False
                    else:
                        exist.add(board[row][col])
        return True
                



