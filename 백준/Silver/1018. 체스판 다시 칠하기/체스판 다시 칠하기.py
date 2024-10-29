def solve():
    n, m = map(int, input().split())
    boards = [input() for _ in range(n)]
    ans = 64
    start_w = "WBWBWBWB"
    start_b = "BWBWBWBW"

    for i in range(n - 7):
        for j in range(m - 7):
            cnt_w = 0; cnt_b = 0
            for x in range(8):
                for y in range(8):
                    if (i + x) % 2 == 0:
                        if boards[i + x][j + y] != start_w[y]:
                            cnt_w += 1
                        if boards[i + x][j + y] != start_b[y]:
                            cnt_b += 1
                    else:
                        if boards[i + x][j + y] != start_b[y]:
                            cnt_w += 1
                        if boards[i + x][j + y] != start_w[y]:
                            cnt_b += 1
            ans = min(ans, cnt_w, cnt_b)

    print(ans)

    
solve()