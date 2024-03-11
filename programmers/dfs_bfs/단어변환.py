"""
https://school.programmers.co.kr/learn/courses/30/lessons/43163
테스트케이스
1. target 단어가 아예 words에 없는 경우
2. words에 있어도 연결 단어가 없을 때 (한 단어만 고쳐서 도달할 수 없는 경우)
방법고안
1. bfs 사용, 하나씩만 변경되는 단어들을 cnt세고, 그 다음으로 올 수 있는 단어들을 cnt하다가, target과 같게 되면 return한다.
어려운 점
1. 글자가 하나만 다른것을 구현하기가 어려웠음
"""
from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0;

    dQ = deque()
    dQ.append((begin,0))

    while dQ :
        word, step = dQ.popleft()
        if word == target:
            return step

        for w in words:
            cnt = 0 # 한 부분만 틀린지 확인할 변수
            for i in range(len(word)):
                if word[i] != w[i]:
                    cnt += 1
            if cnt == 1 :
                dQ.append([w,step+1])  # step이 더 적은게 먼저 들어가므로 최소조건을 만족하게 된다.
    # print("target이 words에 있어도 연결 단어가 없을 때 아래 return 실행")
    return 0

