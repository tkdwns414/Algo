def solve():
    board = [list(map(int, input().split())) for _ in range(5)]
    call = []

    def check(row, col):
        bingo = 0
        # 가로 검사
        for i in range(5):
            if board[row][i] != 0:
                break
            if i == 4:
                bingo += 1
        # 세로 검사
        for i in range(5):
            if board[i][col] != 0:
                break
            if i == 4:
                bingo += 1
        if row == col:
            for i in range(5):
                if board[i][i] != 0:
                    break
                if i == 4:
                    bingo += 1
        if row + col == 4:
            for i in range(5):
                if board[i][4-i] != 0:
                    break
                if i == 4:
                    bingo += 1
        return bingo

    for _ in range(5):
        call += list(map(int, input().split()))


    bingo = 0

    for cnt, number in enumerate(call):
        for i in range(5):
            for j in range(5):
                if board[i][j] == number:
                    board[i][j] = 0
                    bingo += check(i,j)
                    if bingo >= 3:
                        return cnt + 1
    
print(solve())