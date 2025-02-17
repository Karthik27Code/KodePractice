from collections import defaultdict

class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(board)
        cols = len(board[0])
        visited = {}
        crush_set = defaultdict(list)

        def crush(board, r, c):
            val = board[r][c]

            if val != 0:

                r_ind = r + 1
                down_match = 1
                #traverse down
                while r_ind < rows and board[r_ind][c] == val and (r_ind, c) not in visited:
                    down_match += 1
                    visited[(r_ind, c)] = True
                    r_ind += 1
                
                c_ind = c + 1
                right_match = 1
                #traverse right
                while c_ind < cols and board[r][c_ind] == val and (r, c_ind) not in visited:
                    right_match += 1
                    visited[(r, c_ind)] = True
                    c_ind += 1

                
                if down_match >= 3 or right_match >= 3:
                    crush_set[c].append[r]

                if down_match >= 3:
                    r_ind = r + 1
                    while r_ind < rows and board[r_ind][c] == val:
                        crush_set[c].append[r_ind]
                        r_ind += 1

                if right_match >= 3:
                    c_ind = c + 1
                    while c_ind < cols and board[r][c_ind] == val:
                        crush_set[c_ind].append[r]
                        c_ind += 1

                
                visited[(r, c)] = True

        def gravity(board):
            pass


        for r in range(rows):
             for c in range(cols):
                  crush(board, r, c)

        while crush_set:
            visited = {}
            gravity(board)
            crush(board, r, c)

        print(crush_set)


        
        # def isStable(board):


sol = Solution()
sol.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]])


