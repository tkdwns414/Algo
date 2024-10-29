def solve():
    n = int(input())
    cards = set(map(int, input().split()))
    m = int(input())
    f = list(map(int, input().split()))
    print(" ".join("1" if c in cards else "0" for c in f))


solve()