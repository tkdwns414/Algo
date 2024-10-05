def solve():
    N = int(input())
    switches = list(map(int, input().split()))
    s = int(input())
    students = [list(map(int, input().split())) for _ in range(s)]

    for i in range(s):
        switch = students[i][1] - 1 # 기준 스위치 인덱스(번호X)

        if students[i][0] == 1: # 남자면
            for j in range(switch, N, switch + 1): # 배수마다
                switches[j] = 1 - switches[j] # 상태 바꾸기

        else: # 여자면
            step = 0
            while switch - step >= 0 and switch + step < N: # 유효한 동안
                if switches[switch-step] == switches[switch+step]:
                    step += 1
                else:
                    break

            for j in range(switch - step + 1, switch + step):
                switches[j] = 1 - switches[j]
    
    for i in range(N):
        print(f"{switches[i]} ", end = "")
        if (i+1) % 20 == 0:
            print()

solve()
# 시간제한 2초