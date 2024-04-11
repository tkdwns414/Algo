import sys
from collections import Counter

n = int(sys.stdin.readline())
ls = []
for i in range(n):
    ls.append(int(sys.stdin.readline()))

ls.sort()
print(int(round(sum(ls) / n, 0)))  # 산술평균
print(ls[n // 2])  # 중앙값
temp = Counter(ls).most_common()
if len(temp)>1:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(temp[0][0])
print(ls[-1] - ls[0])  # 범위