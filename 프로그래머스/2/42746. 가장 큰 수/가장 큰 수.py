def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers.sort(key = lambda x : x*3, reverse = True)
    
    answer = ''.join(numbers)
    
    if answer.count('0') == len(answer):
        return '0'

    return answer

# 가장 큰 수를 만드는 방법은?
# 문자열로 정렬하여 앞에서부터 붙이기?
# 맨 앞 숫자가 클 수록 앞
# 값이 1000 이하니까 3번 반복하면 누가 큰지 알 수 있다 함 (?)