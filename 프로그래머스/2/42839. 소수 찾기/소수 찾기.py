from itertools import permutations

def solution(numbers):
    numbers = [x for x in numbers]
    answer = 0
    
    def is_prime(n):
        if n <= 1:
            return False
        for d in range(2, int(n**(1/2)) + 1):
            if n % d == 0:
                return False
        return True
    
    num_set = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int("".join(p))
            
            if num not in num_set and is_prime(num):
                num_set.add(num)
                answer += 1
            
    return answer