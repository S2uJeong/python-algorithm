"""
1. 뽑는건 arr[0]에 있을 때 가능
2. 뽑으려는 수가 나올 때 까지 popleft(), append() 반복하고 연산할 때 마다 cnt를 늘려준다.

- 맨 앞에서만 뽑을 수 있는 조건 때문에 조건문의 대소관계를 더 신경써야 했던게 point
- if idx > (len(q) // 2)
"""
from collections import deque
N, M = map(int,input().split())
# 전체 배열 생성 -> 큐(q)로 변환
arr = []
for i in range(N):
    arr.append(i+1)
q = deque(arr)
# 타겟 배열 입력
targets = list(map(int,input().split()))
# ======== 문제 풀이 ============
cnt = 0
for target in targets:
    while True:
        if target == q[0]:
            q.popleft()
            break
        idx = list(q).index(target)
        if idx > (len(q) // 2) : # target이 오른쪽에 더 가까운 경우 (왼쪽은 바로 빼고, 오른쪽은 맨 끝에껄 다시 맨 앞으로 보내고 빼야 하므로 대소관계를 정확히 해야함)
            q.appendleft(q.pop())
            cnt += 1
        else :
            q.append(q.popleft())
            cnt += 1

print(cnt)