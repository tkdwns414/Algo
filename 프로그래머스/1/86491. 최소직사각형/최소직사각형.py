def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

# 가로 세로를 바꿀 수 있음에 주의
# 가능한 가로 길이 가능한 세로 길이 -> 10000 * 10000 -> 너무 오래 걸림
# 가로 세로 구분하지 않고 큰 놈 중에 큰거, 작은 놈 중에 큰거 하면 다 들어감
