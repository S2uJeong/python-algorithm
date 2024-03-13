"""
https://school.programmers.co.kr/learn/courses/30/lessons/42578
공식 : 종류의 개수 + 종류 별 의상 개수끼리의 곱 (1이면 제외)
"""
def solution(clothes):
    dicts = dict() # 의상종류 : 의상 개수
    for _,kind in clothes:
        if kind in dicts:
            dicts[kind] += 1
        else:
            dicts[kind] = 1
    answer = 1
    for kind, val in dicts.items():
        answer *= (val + 1)  # 경우의 수 : (M+1)(N+1) = MN + M + N + 1

    return answer-1 # 아무것도 입지 않은 경우 제외