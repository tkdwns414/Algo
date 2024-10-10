def solve():
    def track(used, results, comparator, idx, ls):
        if k == idx:
            results.add("".join(map(str, ls)))
            return
        for i in range(10):
            if not used[i]:
                if (
                    comparator[idx] == ">" and ls[-1] > i
                    or
                    comparator[idx] == "<" and ls[-1] < i
                ):
                    used[i] = 1; ls.append(i)
                    track(used, results, comparator, idx + 1, ls)
                    used[i] = 0; ls.pop()
        return results

    k = int(input())
    comparator = list(map(str, input().split()))

    res = set()
    for i in range(10):
        used = [0] * 10
        used[i] = 1
        res.update(track(used, set(), comparator, 0, [i]))

    print(max(res))
    print(min(res))

    
solve()

# 21:52 시작
# 22:44 제출
# 완탐 쓰려고 했는데 뭔가 말이 안되는 것 같음. used로 스택으로 푸는게 나을지도?
# 스택으로 푸는 방법을 생각하지 못하겠어서 완탐으로 돌아옴
# 잘못 푼 것 같아서 아예 처음부터 다시 풀기로 수정
# 롤드컵 보면서 풀어서 더 오래 걸린듯...