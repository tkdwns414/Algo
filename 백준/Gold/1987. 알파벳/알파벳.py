def solve():
    r, c = map(int, input().split())
    board = [input() for _ in range(r)]
    
    def is_valid(x, y, visited):
        return (
            0<= x < r 
            and 0<= y < c 
            and board[x][y] not in visited
            )

    dxs = [0, 0, -1, 1]; dys = [-1, 1, 0,0]
    max_move = 0

    # def dfs(x, y, move_cnt):
    #     temp = 0
    #     visited_alpha[board[x][y]] = True
    #     for dx, dy in zip(dxs, dys):
    #         if is_valid(x + dx, y + dy):
    #             temp = max(temp, dfs(x + dx, y + dy, move_cnt + 1))
    #     visited_alpha[board[x][y]] = False
    #     return max(move_cnt, temp)

    # max_move = dfs(0,0,1)

    stack = {(0,0,1,'')}

    while stack:
        x, y, move, visited = stack.pop()
        max_move = max(max_move, move)
        visited += board[x][y]
        for dx, dy in zip(dxs, dys):
            if is_valid(x + dx, y + dy, visited):
                stack.add((x + dx, y + dy, move + 1, visited))
        visited += board[x][y]

    print(max_move)

    
solve()

# 16:39 시작
# 대충 50분?
# visited를 알파벳으로 dictionary로 만들어서 dfs로 가장 큰 값을 구할 수 있을 것 같음
# stack으로 풀려 했는데 visited 관리가 빡세서 그냥 함
# 그런데 재귀로 하니까 시간 너무 길어서 pypy로도 안돼서 stack으로 돌아옴