"""
뒤로 가는 경우의 수 때문에, bfs가 아닌 dfs를 이용해서 문제를 풀었으나 시간초과 뜸
뒤로 가더라도 뒤로 갔다가 점프 하는 경우도 이미 bfs를 통해 탐색이 되므로 bfs로 풀어도 되는 문제였음
"""
from collections import deque


# 입력받기
N, K = map(int, input().split())
# maps - [0] : 왼쪽, [1] : 오른쪽
maps = [[],[]]
for i in range(2):
    tmp = input()
    for j in range(len(tmp)):
        maps[i].append(int(tmp[j]))

# bfs
visited = [[False] * N for _ in range(2)] # visited - [0] : 왼쪽, [1] : 오른쪽
dQ = deque()
dQ.append((0,0,0)) # way(왼/오), k (경과 시간), d (현재 위치)
move = (1,-1,K) # 직진, 후진, 점프
flag = 0
while dQ:
    way, k, d = dQ.popleft()
    for i in range(len(move)):
        nd = d + move[i]

        if nd >= N :
            flag = 1
            break

        if i != 2:
            if nd > k and maps[way][nd] == 1 and not visited[way][nd] : # 불 타 없어질 타일보다 앞이여야 하고, 안전한 곳이여야 하고, 방문하지 않았던 곳이여야 한다.
                dQ.append((way, k+1, nd))
                visited[way][nd] = True
        else :
            if nd > k and maps[1-way][nd] == 1 and not visited[1-way][nd] :
                dQ.append((1-way, k+1, nd))
                visited[1 - way][nd] = True

    if flag == 1:
        break

print(flag)