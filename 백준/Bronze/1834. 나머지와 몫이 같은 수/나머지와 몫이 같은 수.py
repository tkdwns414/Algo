def solve():
    n = int(input())
    sum = 0
    for i in range(n):
        sum += n * i + i
    print(sum)

solve()

# 16:11 시작
# 16:15 제출

# 나머지랑 몫이 같다 -> 나머지의 최대값은 자기자신 -1임
# 거기까지만 검사하면 됨
# 그런데 그냥 해버리면 시간초과 날 수 있음
# 그래서 그냥 구간마다 있는 애들만 계산해서 더해주기