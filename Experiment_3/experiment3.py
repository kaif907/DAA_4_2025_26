def place_markers(n):
    board = [-1] * n

    cols = set()
    diag1 = set()  
    diag2 = set()   

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            board[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            if backtrack(row + 1):
                return True

            board[row] = -1
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return False

    backtrack(0)

    for i in range(n):
        for j in range(n):
            print("1" if board[i] == j else "0", end="")
        print()

place_markers(4)
