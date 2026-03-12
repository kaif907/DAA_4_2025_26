class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m=len(board)
        n=len(board[0])

        def solve(i, j, k):

            if k==len(word):
                return True

            if i<0 or j<0 or i>= m or j>= n:
                return False

            if board[i][j]!=word[k]:
                return False

            temp=board[i][j]
            board[i][j]="#"

            stored_result=(solve(i+1,j,k+1)or
                   solve(i-1,j,k+1)or
                   solve(i,j+1,k+1) or
                   solve(i,j-1,k+1))

            board[i][j] = temp
            return stored_result

        for i in range(m):
            for j in range(n):
                if solve(i, j, 0):
                    return True

        return False
