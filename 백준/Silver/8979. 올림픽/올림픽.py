def solution():
    n, k = map(int, input().split())
    countries = [list(map(int, input().split())) for _ in range(n)]
    countries.sort(key = lambda x : (-x[1], -x[2], -x[3], abs(k - x[0])))
    
    for idx, country in enumerate(countries):
        if country[0] == k:
            return idx + 1
    return 0

print(solution())

# 23:35 시작
# dense rank 아니고 그냥 rank임
# 전체 길이가 1000밖에 안돼서 시간복잡도 신경쓸 필요 없어보임
# 마지막에 나라 번호가 k랑 같은 애가 먼저 나오도록 정렬이 가능한가? >>> abs 이용