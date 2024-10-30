def solution(name):
    answer = 0
    
    for alpha in name:
        answer += min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)
        # 알파벳 변환에 사용되는 횟수
    
    move = len(name) - 1 # 쭉 한 방향으로 갔을 때만 걸리는 횟수
    
    for i in range(len(name)):
        temp = i + 1
        while temp < len(name) and name[temp] == 'A':
            temp += 1 # 다음 바꿔야 할 알파벳 위치
        
        dist = i + len(name) - temp + min(i, len(name) - temp)
        # i 는 오른쪽으로 이동했을 때 횟수
        # len(name) - temp는 처음에 왼쪽으로 이동했을 때 횟수
        # min(i, len(name) - temp)는 처음에 두 방향 중 어디로 간게 더 적게 이동했는지 찾기 위함
        move = min(move, dist)
    
    answer += move
    
    return answer 
