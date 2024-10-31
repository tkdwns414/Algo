from collections import deque

def solution(maps):
    dxys = [[-1,0], [1,0], [0,-1], [0,1]]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    
    def is_valid(x, y):
        return (
            0 <= x < len(maps) and
            0 <= y < len(maps[0])
        )
    
    while queue:
        x, y, level = queue.popleft()
        for dx, dy in dxys:
            if is_valid(x + dx, y + dy) and maps[x + dx][y + dy] != 0 and not visited[x + dx][y + dy]:
                visited[x + dx][y + dy] = True
                maps[x + dx][y + dy] = level + 1
                queue.append((x + dx, y + dy, level + 1))
        
    if visited[len(maps) - 1][len(maps[0]) - 1]:
        return maps[len(maps) - 1][len(maps[0]) - 1]
    return -1