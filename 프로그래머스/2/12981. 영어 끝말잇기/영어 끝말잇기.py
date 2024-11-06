def solution(n, words):
    answer = []
    
    answered = set()
    answered.add(words[0])
    
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1]:
            answer = [i % n + 1, i // n + 1]
            break
        else:
            if words[i] in answered:
                answer = [i % n + 1, i // n + 1]
                break
            answered.add(words[i])
    
    if answer:        
        return answer
    return [0,0]
