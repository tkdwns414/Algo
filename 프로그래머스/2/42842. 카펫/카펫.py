def solution(brown, yellow):
    for r in range(brown // 2 + 2, brown // 4, -1):
        c = brown // 2 + 2 - r
        if (r-2) * (c-2) == yellow:
            return [r, c]

    return []

## 갈색 격자의 수 가로를 x, 세로를 y라 할 때 전체 타일 개수가 n이라면
# 그 때 노랑 격자의 가로 세로 수는 x - 2, y - 2
# 2x + 2y - 4 = n -> x + y = n//2 + 2
# 근데 가로가 더 기니까 그거 생각해서 돌기