from collections import defaultdict
from typing import List

''' 
This solution works but the space complexity can be improved. 
Space complexity is O(n^2).
'''
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

''' 
This solution improves the space complexity by using bit masking using &(and) and |(or) bitwise operators. 
Space complexity is O(n).
'''
class Solution2:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        cols = [0] * N
        rows = [0] * N
        box = [0] * N

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]

                if num != '.':
                    num = int(num) - 1

                    #check in column
                    if cols[c] & (1 << num):
                        return False
                    else:
                        cols[c] = cols[c] | (1 << num)

                    #check in row
                    if rows[r] & (1 << num):
                        return False
                    else:
                        rows[r] = rows[r] | (1 << num)

                    #check in box
                    box_index = (r // 3) * 3 + (c // 3)
                    if box[box_index] & (1 << num):
                        return False
                    else:
                        box[box_index] = box[box_index] | (1 << num)

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


sol1 = Solution()
sol2 = Solution2()

assert sol1.isValidSudoku(board_1) != False, "Assertion fail, this is a valid board"
assert sol2.isValidSudoku(board_1) != False, "Assertion fail, this is a valid board"

assert sol1.isValidSudoku(board_2) != True, "Assertion fail, this is an invalid board"
assert sol2.isValidSudoku(board_2) != True,  "Assertion fail, this is an invalid board"