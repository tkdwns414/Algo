def solve():
    n = int(input())
    map_size = 4 * n - 3
    star_map = [[" "] * map_size for _ in range(map_size)]

    def star(start, end):
        for i in range(start, end):
            for j in range(start, end):
                if i == start or i == end - 1:
                    star_map[i][j] = "*"
                elif j == start or j == end - 1:
                    star_map[i][j] = "*"
    
    step = 0
    while step <= map_size//2:
        star(step, map_size - step)
        step +=  2


    for stars in star_map:
        print("".join(stars))
    

solve()

# n 이 늘어날 때 4개 별 줄이 생김
# 그러니까 전체 길이는 An = 4n - 3

