def solve():
    n, m = map(int, input().split())
    castles = [input() for _ in range(n)]


    column_blank = []
    for i in range(n):
        check = False
        for j in range(m):
            if castles[i][j] == "X":
                check = True
        if not check:
            column_blank.append(i)

    row_blank = []
    for i in range(m):
        check = False
        for j in range(n):
            if castles[j][i] == "X":
                check = True
        if not check:
            row_blank.append(i)

    print(max(len(column_blank),len(row_blank)))


solve()

# 비어있는 행, 비어있는 열 구해오기
# 비어있는 행 + 비어있는 열 에서 중복 제거하기
# 라고 생각했었는데 그냥 둘 중 더 많이 커버 필요한 애를 커버하면서 다 커버 가능