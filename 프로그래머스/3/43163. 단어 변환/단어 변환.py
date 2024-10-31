from collections import deque

def solution(begin, target, words):
    visited = [False] * len(words)
    queue = deque([(begin, 0)])
    
    def accessible(word1, word2):
        check = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                check += 1
            if check > 1:
                return False
        return True if check == 1 else False
        
    
    while queue:
        current, level = queue.popleft()
        if current == target:
            return level
        for idx, word in enumerate(words):
            if not visited[idx] and accessible(current, word):
                visited[idx] = True
                queue.append((word, level + 1))
                             
    return 0