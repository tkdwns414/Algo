def solution(people, limit):
    answer = 0; front = 0; rear = len(people) - 1
    people.sort(reverse = True) 
    
    while front <= rear:
        if people[front] + people[rear] <= limit:
             # 어차피 두 명만 탈 수 있으니까 지금 젤 무거운 애랑 젤 가벼운 애랑 같이 탈 수 있는지 비교
            rear -= 1
        front  += 1
        answer += 1
        
    return answer

# 어떻게 해야지 구명보트에 효과적으로 채울 수 있는지?
# 구명보트 최대 2명만 가능
# 뒤에서부터 탈 수 있는 애들 더해서 찾기 -> 그냥 정렬을 뒤집어서 하는게 나을듯
