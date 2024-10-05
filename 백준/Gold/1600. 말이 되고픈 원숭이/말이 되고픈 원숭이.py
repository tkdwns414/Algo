from collections import deque

def solve():
    k = int(input())
    w, h = map(int, input().split())
    explore = [list(map(int, input().split())) for _ in range(h)]
    visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
    
    def is_valid(x, y):
        return 0 <= x < h and 0 <= y < w and explore[x][y] != 1

    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 1

    dxs = [0, 0, 1, -1]; dys = [1, -1, 0, 0]
    hdxs = [-2, -2, -1, -1, 1, 1, 2, 2]; hdys = [1, -1, 2, -2, 2, -2, 1, -1]

    while queue:
        cur_x, cur_y, cur_h = queue.popleft()
        if cur_x == h - 1 and cur_y == w - 1:
            return visited[cur_x][cur_y][cur_h] - 1

        for dx, dy in zip(dxs, dys):
            if is_valid(cur_x + dx, cur_y + dy) and visited[cur_x + dx][cur_y + dy][cur_h] == 0:
                visited[cur_x + dx][cur_y + dy][cur_h] = visited[cur_x][cur_y][cur_h] + 1
                queue.append([cur_x + dx, cur_y + dy, cur_h])
        
        if cur_h < k:
            for dx, dy in zip(hdxs, hdys):
                if is_valid(cur_x + dx, cur_y + dy) and visited[cur_x + dx][cur_y + dy][cur_h + 1] == 0:
                    visited[cur_x + dx][cur_y + dy][cur_h + 1] = visited[cur_x][cur_y][cur_h] + 1
                    queue.append([cur_x + dx, cur_y + dy, cur_h + 1])
        
    return -1

print(solve())
