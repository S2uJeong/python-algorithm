"""
치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
기존의 치킨집을 M개로 줄이는데, 도시의 치킨 거리가 가장 작게 되는 것을 고려하여 삭제

1. 집과 가장 가까운 치킨집을 찾는다 : bfs
2. M의 위치에 따라 달라지는 결과값을 보고 result를 반환한다.
    - if M <= 원래 있던 치킨집 수 : 거리 계산 후 return
    - dfs를 통해 원래 치킨집이 있던 위치 list에서 경우의 수를 구해 진행
"""
import sys
input = sys.stdin.readline


def cal_chicken_distance(house_xy, selected_chicken_xy):  # 거리 구하는 거, 가장 가까이에 있는 치킨집으로 구한다는 생각에 bfs 사용 했다가 오히려 속도 느려짐..
    result = 0
    for hr,hc in house_xy:
        min_dist = 10e9
        for cr,cc in selected_chicken_xy:
            dist = abs(hr-cr) + abs(hc-cc)
            min_dist = min(min_dist, dist)
        result += min_dist
    return result

def dfs_for_chicken_location(idx, visited_chick): # idx를 사용해 현재 치킨집을 사용하냐 안 하느냐로 dfs 구성
    global answer

    if len(visited_chick) == M:
        answer = min(cal_chicken_distance(house_xy, visited_chick), answer)
        return
    if idx == len(chicken_xy):
        return
    # 현재 치킨집을 선택하는 경우
    visited_chick.append(chicken_xy[idx])
    dfs_for_chicken_location(idx+1, visited_chick)
    # 안 하는 경우
    visited_chick.pop()
    dfs_for_chicken_location(idx+1, visited_chick)


N, M = map(int,input().split())
chicken_xy = []
house_xy = []
# 주어진 값을 판별해 type별 list에 좌표 추가
for i in range(N):
    tmp_list = list(map(int,input().split()))
    for j in range(len(tmp_list)):
        if tmp_list[j] == 2 :
            chicken_xy.append((i,j))
        elif tmp_list[j] == 1 :
            house_xy.append((i,j))

answer = 10e9
if len(chicken_xy) <= M :
    print(cal_chicken_distance(house_xy, chicken_xy))
else:
    dfs_for_chicken_location(0,[])
    print(answer)