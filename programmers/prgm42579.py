"""
베스트앨범
https://programmers.co.kr/learn/courses/30/lessons/42579
"""

def solution(genres, plays):
    answer = []
    music_play = {}
    total = {}
    idx = 0
    for g, p in zip(genres, plays):
        if g not in music_play:
            music_play[g] = [(p, idx)]
            total[g] = p
        else:
            music_play[g].append((p, idx))
            total[g] += p
        idx += 1

    total = sorted(total.items(), key = lambda x : x[1], reverse = True)
    
    for t in total:
        
        playlist = sorted(music_play[t[0]], key = lambda x : x[0], reverse = True)
        if len(playlist) == 1:
            answer.append(playlist[0][1])
        else:
            answer.append(playlist[0][1])
            answer.append(playlist[1][1])
            
    return answer
