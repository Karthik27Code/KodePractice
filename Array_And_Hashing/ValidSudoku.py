from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(dict)
        rows = defaultdict(dict)
        box = defaultdict(dict)
        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                box_r = r // 3
                box_c = c // 3
                if num != '.':
                    if num in cols[c] or num in rows[r] or num in box[(box_r,box_c)]:
                        return False
                    else:
                        cols[c][num] = True
                        rows[r][num] = True
                        box[(box_r,box_c)][num] = True

        return True
    

board_1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


board_2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]