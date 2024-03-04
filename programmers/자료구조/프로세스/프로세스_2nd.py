"""
https://school.programmers.co.kr/learn/courses/30/lessons/42587
1. 로직
   1-1. arr[idx] == max_value  &&  idx == location :  cnt 반환, break
   1-2. arr[idx] == max_value  : cnt ++, 최대값 찾기
   1-3. 우선순위가 아닌 프로세스는 다시 맨 뒤로 가게 된다.
2. 자료구조
   - deque
"""

""" location은 dQ에 idx,val을 같이 넣어 해결, 정렬해서 최댓값 얻어냄 
dQ = deque()
for idx, val in enumerate(priorities):
    dQ.append((idx, val))
max_val = sorted(list(dQ), key=lambda x: -x[1])[0][1]
print(max_val)
"""
from collections import deque
def solution(priorities, location):
    dQ = deque()
    cnt = 0

    for idx,val in enumerate(priorities):
        dQ.append((idx,val))

    max_val = sorted(list(dQ), key=lambda x: -x[1])[0][1]

    while dQ :
        idx, val = dQ.popleft()
        if val == max_val and idx == location:
            cnt += 1
            return cnt

        if val == max_val:
            cnt += 1
            max_val = sorted(list(dQ), key=lambda x : -x[1])[0][1]
            continue

        dQ.append((idx,val))

    return -1
