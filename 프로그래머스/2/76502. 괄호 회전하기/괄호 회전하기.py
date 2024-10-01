def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        check = True;
        for j in range(len(s)):
            c = s[(i+j)%len(s)]
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack:
                    check = False
                    break
                    
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    check = False
                    break
        
        if not stack and check:
            answer += 1
            
    return answer