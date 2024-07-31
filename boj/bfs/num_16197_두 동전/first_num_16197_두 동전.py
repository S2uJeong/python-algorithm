from collections import deque

N, M = map(int, input().split())
start_point = []
maps = [list(input().strip()) for i in range(N)]


# 동전이 있는 좌표 확인 len(start_point) == 2
for i in range(len(maps)):
    for j in range(len(maps[i])):
        if maps[i][j] == 'o':
            start_point.append([i, j])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
start_point.append(0)
dQ = deque([start_point])
print(list(dQ))

while dQ:
    coin1, coin2, cnt = dQ.popleft()

    if cnt > 10:
        print(-1)
        break

    if not ( (0 <= coin1[0] < N and 0 <= coin1[1] < M) and (0 <= coin2[0] < N or 0 <= coin2[1] < M)):  # 동전이 두개 다 위에 있는거 아니면 return
        print(cnt)

    # 이동하며 확인
    for k in range(4):
        n_coin1 = [coin1[0] + dr[k], coin1[1] + dc[k]]
        n_coin2 = [coin2[0] + dr[k], coin2[1] + dc[k]]

        if ((N <= n_coin1[0] < 0 or M <= n_coin1[1] < 0) and (
                N <= n_coin2[0] < 0 or M <= n_coin2[1] < 0)):  # 동전이 두개 다 떨어지는 상황
            continue
        else:
            # IndexError: list index out of range 발생.. 실패
            if (maps[n_coin1[0]][n_coin1[1]] == '#') and (maps[n_coin2[0]][n_coin2[1]] == '#'):
                continue
            elif (maps[n_coin1[0]][n_coin1[1]] != '#'):
                cnt += 1
                dQ.append([coin1, n_coin2, cnt])
            elif (maps[n_coin2[0]][n_coin2[1]] != '#'):
                cnt += 1
                dQ.append([n_coin1, coin2, cnt])
            else:
                cnt += 1
                dQ.append([coin1, coin2, cnt])



