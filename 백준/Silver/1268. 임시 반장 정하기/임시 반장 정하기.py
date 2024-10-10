def solve():
    n = int(input())
    childs_classes = [list(map(int, input().split())) for _ in range(n)]
    child_meets = [[i, set()] for i in range(n)] # i번 학생과 친구들

    for i in range(n):
        for j in range(n):
            for k in range(5):
                if childs_classes[i][k] == childs_classes[j][k]:
                    child_meets[i][1].add(j)

    child_meets.sort(key = lambda x: (len(x[1]), -x[0]), reverse=True)
    print(child_meets[0][0] + 1)

solve()

# 처음엔 어떤 학생이 어떠한 반들에 속했는지 알려줌
# 마지막에 가지고 있어야할건 어떤 학생이 그동안 같은 반 했던 아이의 수
# '몇학년 몇반에 몇명'을 구하기
# 애들을 하나하나 돌면서 자기가 속했던 반에 몇명이 있었는지 구하기
# 정렬

## 가장 많이 같은 반을 한게 중요한게 아니라 가장 많이 아는 친구가 중요한거임...
# 1번 학생부터 자기랑 같은 반이었던 애들을 저장하는 함수를 만들기
# 그냥 for문 3번으로 돌기 = 1000 * 1000 * 5 < 2초