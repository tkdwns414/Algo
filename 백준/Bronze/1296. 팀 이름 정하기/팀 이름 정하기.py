from collections import Counter

def solve():
    name = input()
    name_count = Counter(name)
    t = int(input())
    teams = []
    for _ in range(t):
        temp = input()
        temp_count = Counter(temp)
        temp_score = score(
            name_count["L"] + temp_count["L"],
            name_count["O"] + temp_count["O"],
            name_count["V"] + temp_count["V"],
            name_count["E"] + temp_count["E"]
        )
        teams.append((temp, temp_score))
    
    teams.sort(key = lambda x: (-x[1], x[0]))
    print(teams[0][0])

def score(l, o, v, e):
    return (
            (l + o) #% 100
            * (l + v) #% 100
            * (l + e) #% 100
            * (o + v) #% 100
            * (o + e) #% 100
            * (v + e) % 100
        )

solve()

# 대문자인거 잘 보기 + 필요시 오버플로우 방지