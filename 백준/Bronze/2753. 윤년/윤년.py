def solve(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1
    return 0

year = int(input())
print(solve(year))