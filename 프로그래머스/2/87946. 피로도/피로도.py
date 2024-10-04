def solution(k, dungeons):
    visited = [0] * len(dungeons)
    answer = explore(k, visited, dungeons, 0)
    return answer

def explore(cur_k, visited, dungeons, cnt): # 현재 피로도, 방문 여부, 던전 정보, 지금까지 방문한 수
    temp = cnt
    for i in range(len(dungeons)):
        if visited[i] == 0 and cur_k >= dungeons[i][0]: # 방문할 수 있다면
            visited[i] = 1
            temp = max(temp, explore(cur_k - dungeons[i][1], visited, dungeons, cnt + 1))
            visited[i] = 0
    return temp