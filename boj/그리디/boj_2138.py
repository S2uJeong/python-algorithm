"""
N^2 알고리즘 가능하다. 2초, 100,000^2

경우의 수를 해야 하는 거라 당연히 재귀함수를 써야할 것 같은데,, 이중 for문으로 구성해야 겠다.
- 경우의 수를 알아본다고 해도 어떤 순서로 어떤 규칙으로 바꾸어 나갈지가 고민임
    - 탐색 기준
        - idx에서 서로 다르다면, 바꿔줘야 한다는 신호이므로 i-1, i, i+1 중에 골라서 진행시킴.
        - 왼 -> 오
    - 실패점
        - 똑같아질때까지 비교하고 돌려볼 수 밖에 없어서 문제해결이 안됨
- 그리디
    - 탐색 기준
        - 전구의 상태변화를 순차적으로 계산하며
        - i번째 스위치는 i-1번째 전구의 상태를 결정할 마지막 스위치 라는 것에만 초점.
"""
import sys
input = sys.stdin.readline
# 입력
N = int(input().rstrip())
status = list(map(int,input().rstrip()))
target = list(map(int,input().rstrip()))

MAX = int(1e9)

def turn(now, i): # int list를 기준으로 1 -> 0 , 0 -> 1 로 바꿔주며, if문으로 index out을 막았다.
    now[i] = 1-now[i]
    now[i-1] = 1-now[i-1]
    if (i+1 < N):
        now[i+1] = 1-now[i+1]
    return now

def turn_switch(status):
    cnt = 0
    now = status[:]
    for i in range(1,N):
        if now[i-1] == target[i-1]:
            continue
        cnt += 1
        now = turn(now, i)

    if now == target:
        return cnt

    return MAX

caseAResult = turn_switch(status)

status[0] = 1 - status[0]
status[1] = 1 - status[1]
result = min(caseAResult, turn_switch(status) + 1)
if result == MAX:
    print(-1)
else:
    print(result)


