def solution(sound):
    if len(sound) % 5 != 0:
        return -1
    
    quack = 'quack'
    visited = [0 for _ in range(len(sound))]
    duck = 0
    for i in range(len(sound)):
        if visited[i] == 0 and sound[i] == 'q':
            duck += 1
            state = 1
            visited[i] = duck
            for j in range(i + 1, len(sound)):
                if visited[j] == 0 and sound[j] == quack[state]:
                    visited[j] = duck
                    state = (state + 1) % 5
            if state != 0:
                return -1
    
    if 0 in visited:
        return -1
    return duck


sound = input()
print(solution(sound))