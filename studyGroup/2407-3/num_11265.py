"""
단방향 그래프, 가중치 있음
파티장에서 다른 파티장까지 시간 내에 도착할 수 있는지

1. 노드별 쌍으로 최단 거리를 구한다. (플로이드 워셜)
2. 해당 최단 시간이 주어진 시간보다 작으면 갈 수 있다.

노드가 500개 이하이므로 플로이드 워셜을 써서 해결한다.
dp 리스트가 따로 필요할 줄 알았는데 필요 없었다!
"""
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

# 플로이드 워셜로 최단거리 업데이트
for k in range(N):
    for i in range(N):
        for j in range(N):
            maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])

# input 받아 결과 출력
for _ in range(M):
    start, arrival, available_time = map(int,input().split())
    if maps[start-1][arrival-1] <= available_time:
        print("Enjoy other party")
    else :
        print("Stay here")
