def solution(genres, plays):
    answer = []
    
    genre_music = {g : [] for g in set(genres)}
    genre_played = {g : 0 for g in set(genres)}
    
    for i in range(len(plays)):
        genre_music[genres[i]].append([i, plays[i]])
        genre_played[genres[i]] += plays[i]
        
    for g in sorted(genre_played, key = lambda x: genre_played[x], reverse = True):
        genre_music[g].sort(key = lambda x: (x[1], -x[0]), reverse = True)
        answer += [m[0] for m in genre_music[g][:2]]
    
    return answer

# 어떤 장르가 제일 많은지, 장르별 숫자 하기
# 그럼 장르별 [음원 번호, 플레이]