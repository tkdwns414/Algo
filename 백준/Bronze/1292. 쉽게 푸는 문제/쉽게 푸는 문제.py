def solve():
    cnt = 1; i = 1
    answer = [0]
    while cnt < 1000:
        for _ in range(i):
            answer.append(answer[-1] + i)
            cnt += 1
        i += 1

    a, b = map(int, input().split())
    print(answer[b] - answer[a-1])


solve()
