"""
완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576
"""
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     answer = participant[-1]
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return answer

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]