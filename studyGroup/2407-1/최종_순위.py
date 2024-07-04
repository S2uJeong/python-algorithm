"""
시간복잡도 : 1초 제한
- 테스트 케이스 1 ~ 100
- 팀의 수 2 ~ 500
- 등수가 바뀐 쌍의 수 0 ~ 25000 : 0이면 이전 등수 그대로 출력

출력은 세가지 경우가 있다.
1. 팀이 순위대로 잘 정렬된 경우
2. 데이터 일관성이 깨진 경우 : 사이클이 발생하면 큐에 아무원소도 들어갈 수 없다.
3. 순위를 정확히 모르는 경우 : 한 번에 2개 이상의 원소가 들어간다는 것, 진입차수가 0인 원소가 두개 이상이 되므로 순위를 정할 수 없는 경우가 된다.

고민점
출력 조건에 따라 어떤 결과물이 나올 수 있는지 예측하는게 어려웠음
이전 등수까지 간선으로 표현해준뒤, 위상정렬을 이어가는게 포인트
"""
from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip()) # 테스트 케이스 개수
for _ in range(T):
    N = int(input().rstrip()) # 팀 개수
    pre_records = list(map(int,input().split())) # 이전 대회에서 등수 기준으로 정렬된 팀 번호
    # 이전 등수를 바탕으로 간선 표시
    graph = [[] for _ in range(1 + N)]  # graph[i] 안에 i번째 팀 보다 뒷 순위인 팀들의 번호가 들어감
    depth = [0] * (N + 1)  # 상대 순위 깊이 표시 (idx = 팀 번호)
    for i in range(N-1):
        for j in range(i+1, N):
            graph[pre_records[i]].append(pre_records[j])
            depth[pre_records[j]] += 1

    K = int(input().rstrip()) # 순위 변동건수
    for _ in range(K):
        winner, loser = map(int,input().split())
        flag = True # False : 이전 등수를 바탕으로, 이번에 진팀이 이전에도 winner보다 뒤에 있던 경우 => 잘못된 정보이므로 사이클을 발생시킨다

        for later_team in graph[winner]:
            if later_team == loser:
                # 이전 등수가 오정보라고 치고, 반대로 간선을 update한다.
                graph[winner].remove(loser)
                depth[loser] -= 1
                graph[loser].append(winner)
                depth[winner] += 1
                flag = False

        if flag:
            # 이전 등수에 반영 되어 있던것 삭제
            graph[loser].remove(winner)
            depth[winner] -= 1
            # 이번 등수에 맞게 삽입
            graph[winner].append(loser)
            depth[loser] += 1

    dQ = deque()
    for i in range(1, N+1):
        if depth[i] == 0:
            dQ.append(i)

    if not dQ:
        print("IMPOSSIBLE")
        continue

    is_impossible = False
    result = []
    while dQ:
        if len(dQ) > 1 :
            is_impossible = True
            break

        crt_team = dQ.popleft()
        result.append(crt_team)

        for later_team in graph[crt_team]:
            depth[later_team] -= 1
            if depth[later_team] == 0 :
                dQ.append(later_team)
            elif depth[later_team] < 0 :
                is_impossible = True
                break
    if is_impossible or len(result) < N :
        print("IMPOSSIBLE")
    else:
        print(*result)
