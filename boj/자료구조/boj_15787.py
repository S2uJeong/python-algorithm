"""
기차에 명령을 deque로 표현하고 0 20개 좌석을 다 초기화
- 1,2번 명령 땐 idx 탐색으로 확인 O(N) : dQ[idx] = 1
- 3번 명령 땐 appendleft(0), pop()
- 4번 명령 땐 append(0), popleft()

기차 개수 * 좌석 개수 = 2,000,000
이중 for문으로 탐색 시 : 4,000,000,000,000
- 사람이 있는 좌석번호만 list(n)에 적어 둔 뒤, 비교 한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M  = map(int,input().split()) # 기차의 수, 명령의 수
trains = [deque([0] * 20) for _ in range(N)]

for _ in range(M):
    in_list = list(map(int,input().split()))
    if in_list[0] <= 2 :
        amend, n, x = in_list
        if amend == 1: # 태운다
            trains[n-1][x-1]  = 1 # 자료 idx를 맞춰 주기 위해  -1 해서 탐색
        else :
            trains[n-1][x-1]  = 0
    else:
        amend, n = in_list
        if amend == 3:
            trains[n-1].appendleft(0)
            trains[n-1].pop()
        else :
            trains[n-1].append(0)
            trains[n-1].popleft()

# 각 기차별로 idx를 2^idx 이라고 생각하고 모든 값을 더한 것을 result에 넣는다. => 예외 : idx 0 은 1이다.
# result 를 set으로 중복제거 한 뒤, len을 반환한다.
result = []
for train in trains:
    sum = 0
    # idx 0에 대해 미리 더함
    if train[0] == 1 :
        sum += 1

    for i in range(1,len(train)):
        if train[i]: # 해당 좌석에 사람이 있으면 1
            sum += (2**i)

    result.append(sum)

answer = set(result)
print(len(answer))