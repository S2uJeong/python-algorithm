import sys
sys.setrecursionlimit(10**7)

def dfs(way, maps, k, d): # 왼or오, 맵, 경과 시간(초), 현재 위치
    global flag

    if d >= N-1:
        flag = 1
        return   # 게임 클리어

    if k > N :
        return # 끝까지 갈 때까지 클리어 못함

    # flag가 flase이면 진행
    if not flag:
        # 3가지 방향으로 dfs 진행
            # 직진
        if maps[way][d+1] == 1:
            dfs(way, maps, k+1, d+1)
            # 뒤로 가는 방향 - 이미 불탄 곳으로 못가게
        if d-1 > k and maps[way][d-1] == 1:
            dfs(way, maps, k+1, d-1)
            # 점프 - out_of_index 방지
        if d+K >= N-1:
            flag = 1
            return
        elif maps[1-way][d+K] == 1:
            dfs(1-way, maps, k+1, d+K)

    return flag


# 입력받기
N, K = map(int, input().split())
maps = [[],[]]
for i in range(2):
    tmp = input()
    for j in range(len(tmp)):
        maps[i].append(int(tmp[j]))

flag = 0
result = dfs(0,maps,0,0)
print(result)
