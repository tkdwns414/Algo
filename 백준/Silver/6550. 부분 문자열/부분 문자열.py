def solve():
    s, t = input().split()
    step = 0

    for char in t:
        if char == s[step]:
            step += 1
            if step == len(s):
                print("Yes")
                return
    
    
    print("No")

while True:
    try:
        solve()
    except:
        break
