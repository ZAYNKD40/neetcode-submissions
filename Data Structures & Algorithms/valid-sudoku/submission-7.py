class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #set to hold the shapes, define them
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        #double loop to traverse 2d sudoku board
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                # if the number is duplicate and already exist
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)]. add(board[r][c])
                #3 by 3 square, the hashset is storing square key as 0,0; 0,1;2,2 etc each key in 
                #cols rows squares though can hold up to 9 values
        #if pass all trials for False return true
        return True

        